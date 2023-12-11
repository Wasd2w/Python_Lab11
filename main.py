import csv

def process_csv(input_file, output_file):
    try:
        with open(input_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)

        print("Original CSV File:")
        for row in rows:
            print(row)

        usa_data = [row for row in rows if row['Country'] == 'United States' and row['Year'] == '2019']
        ukraine_data = [row for row in rows if row['Country'] == 'Ukraine' and row['Year'] == '2019']

        comparison_result = [
            {
                'Year': usa_row['Year'],
                'GDP (USA)': usa_row['Value'],
                'GDP (Ukraine)': ukraine_row['Value'],
            }
            for usa_row, ukraine_row in zip(usa_data, ukraine_data)
        ]

        fieldnames = ['Year', 'GDP (USA)', 'GDP (Ukraine)']
        with open(output_file, 'w', newline='') as output_csv:
            writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(comparison_result)
        print(f"Comparison result saved to '{output_file}' successfully.")
    except Exception as e:
        print(f"Error processing files: {e}")

input_file_name = 'input_file.csv'
output_file_name = 'comparison_result.csv'

process_csv(input_file_name, output_file_name)
