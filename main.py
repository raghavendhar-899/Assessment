import csv
import sys
from collections import defaultdict

def load_lookup_table(lookup_file):
    lookup = {}
    try:
        with open(lookup_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Combine port and protocol to create a unique key
                key = (row['dstport'], row['protocol'].lower())
                lookup[key] = row['tag']
    except FileNotFoundError:
        print(f"Error: The lookup file '{lookup_file}' was not found.")
        exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the lookup file: {e}")
        exit(1)
    return lookup

def parse_flow_logs(flow_file, lookup):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    try:
        with open(flow_file, mode='r') as file:
            for line in file:
                parts = line.split()
                if len(parts) < 10:
                    if len(parts)!=0:
                        print(f"Warning: Skipping line with insufficient fields: {line.strip()}")
                    continue  # Skip lines that don't have enough fields

                dstport = parts[5]
                protocol_num = parts[7]
                
                # Map protocol number to name (6 -> tcp, 17 -> udp, 1 -> icmp)
                protocol_map = {
                    '6': 'tcp',
                    '17': 'udp',
                    '1': 'icmp'
                }
                protocol = protocol_map.get(protocol_num, '').lower()
                if not protocol:
                    print(f"Warning: Unsupported protocol number '{protocol_num}' in line: {line.strip()}")
                    continue

                key = (dstport, protocol)

                # Check if there's a matching tag
                tag = lookup.get(key, 'Untagged')

                # Increment the count for the tag
                tag_counts[tag] += 1
                # Increment the count for the port/protocol combination
                port_protocol_counts[key] += 1

    except FileNotFoundError:
        print(f"Error: The flow log file '{flow_file}' was not found.")
        exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the flow log file: {e}")
        exit(1)

    return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts, output_file):
    try:
        with open(output_file, mode='w') as file:
            file.write("Tag,Count\n")
            for tag, count in sorted(tag_counts.items()):
                file.write(f"{tag},{count}\n")

            file.write("\nPort,Protocol,Count\n")
            for (port, protocol), count in sorted(port_protocol_counts.items()):
                file.write(f"{port},{protocol},{count}\n")

    except Exception as e:
        print(f"Error: An unexpected error occurred while writing to the output file: {e}")
        exit(1)

def main():
    
    lookup_file = 'lookup_table.csv'
    flow_file = 'flow_logs.txt'
    output_file = 'output.txt'

    # Check for command-line arguments and assign custom files
    if len(sys.argv) > 1:
        lookup_file = sys.argv[1]
    if len(sys.argv) > 2:
        flow_file = sys.argv[2]
    if len(sys.argv) > 3:
        output_file = sys.argv[3]

    # Load the lookup table
    lookup = load_lookup_table(lookup_file)

    # Parse the flow logs and get the counts
    tag_counts, port_protocol_counts = parse_flow_logs(flow_file, lookup)

    # Write the output to a file
    write_output(tag_counts, port_protocol_counts, output_file)

    print(f"Output successfully written to {output_file}")

if __name__ == "__main__":
    main()
