import pandas as pd

# Load the CSV file
file_path = 'payment-methods.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Start the HTML content with styling
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment Methods Table</title>
    <style>
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
    }

    th,
    td {
      padding: 10px;
      vertical-align: middle;
      text-align: left;
    }

    th {
      font-size: 13px
    }

    td:first-child {
      width: 150px;
    }

    .payment-method-container {
      display: inline-flex;
      align-items: center;
    }

    .payment-method-container img {
      width: 35px;
      height: auto;
      margin-right: 10px;
    }

    .payment-name {
      font-weight: bold;
    }

    .payment-category {
      font-size: small;
      color: grey;
    }

    /* Styles for "show more" functionality */
    .extra-content {
      display: none;
    }

    .show-more-label {
      color: blue;
      cursor: pointer;
      font-size: 0.9em;
    }

    /* Hide the checkbox */
    .show-more-checkbox {
      display: none;
    }

    /* Show extra content and hide label when checkbox is checked */
    .show-more-checkbox:checked+.show-more-label {
      display: none;
    }

    .show-more-checkbox:checked+.show-more-label+.extra-content {
      display: inline;
    }


    /* Styles for "show more" functionality */
    .extra-content-2 {
      display: none;
    }

    .show-more-label-2 {
      color: blue;
      cursor: pointer;
      font-size: 0.9em;
    }

    /* Hide the checkbox */
    .show-more-checkbox-2 {
      display: none;
    }

    /* Show extra content and hide label when checkbox is checked */
    .show-more-checkbox-2:checked+.show-more-label-2 {
      display: none;
    }

    .show-more-checkbox-2:checked+.show-more-label-2+.extra-content-2 {
      display: inline;
    }
  </style>
</head>
<body>

<table>
    <tr>
        <th>Payment Method</th>
        <th>Payer Country</th>
        <th>Business Registration Country</th>
    </tr>
'''

for index, row in data.iterrows():
    
    #countries = sorted(row["Country of business registration"].split(', '))
    countries = sorted([country.strip() for country in row["Country of business registration"].split(', ')])

    if len(countries) <= 4:
        # If 4 or fewer countries, display all directly
        country_business_registration = f'''
            <td>{row["Country of business registration"]}</td>
        '''
    else:
        # If more than 4 countries, use the "Show More" functionality
        initial_countries = ', '.join(countries[:4])
        extra_countries = ', '.join(countries[4:])
        country_business_registration = f'''
        <td>
            {initial_countries}
            <input type="checkbox" class="show-more-checkbox" id="show-more-{index}">
            <label for="show-more-{index}" class="show-more-label">Show More</label>
            <span class="extra-content">, {extra_countries}</span>
        </td>
        '''

    # Split the "Payer's country" column to get the individual countries
    #countries_2 = sorted(row["Payer's country"].split(', '))
    countries_2 = sorted([country.strip() for country in row["Payer's country"].split(', ')])
    
    if len(countries_2) <= 4:
        # If 4 or fewer countries, display all directly
        payer_country_content = f'''
            <td>{row["Payer's country"]}</td>
        '''
    else:
        # If more than 4 countries, use the "Show More" functionality
        initial_countries_2 = ', '.join(countries_2[:4])
        extra_countries_2 = ', '.join(countries_2[4:])
        payer_country_content = f'''
        <td>
            {initial_countries_2}
            <input type="checkbox" class="show-more-checkbox-2" id="show-more-{index*1000}">
            <label for="show-more-{index*1000}" class="show-more-label-2">Show More</label>
            <span class="extra-content-2">, {extra_countries_2}</span>
        </td>
        '''
    
    html_content += f'''
    <tr>
        <td>
            <div class="payment-method-container">
                <img src="{row['Logo']}" alt="{row['Payment method name']}">
                <div>
                    <div class="payment-name">{row['Payment method name']}</div>
                    <div class="payment-category">{row['Category']}</div>
                </div>
            </div>
        </td>
        {payer_country_content}
        <td>
            {initial_countries}
            <input type="checkbox" class="show-more-checkbox" id="show-more-{index}">
            <label for="show-more-{index}" class="show-more-label">Show More</label>
            <span class="extra-content">, {extra_countries}</span>
        </td>
    </tr>
    '''

    
# Close the HTML content
html_content += '''
</table>

</body>
</html>
'''

# Save the HTML content to a file
with open('payment_methods_table.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print(html_content)
