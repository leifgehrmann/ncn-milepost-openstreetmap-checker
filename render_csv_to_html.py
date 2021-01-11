import csv
import os
import shutil

# 1. Copy contents of public into dist
public_dir = 'public/'
dist_dir = 'dist/'
if os.path.exists(dist_dir):
    shutil.rmtree(dist_dir)
shutil.copytree(public_dir, dist_dir)

# 2. Read index.html
with open(dist_dir + 'index.html') as file:
    index_html = file.read()

# 3. Parse CSV and convert CSV row to HTML, and append to string
with open('output.csv', newline='') as csv_file:
    milepost_csv = csv.reader(
        csv_file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL
    )

    milepost_html = ''
    row_number = 0
    for milepost_data_row in milepost_csv:
        row_number += 1
        if row_number == 1:
            milepost_html += '<thead><tr><th>' + '</th><th>'.join(milepost_data_row) + '</th></tr></thead>'
            continue
        if row_number == 2:
            milepost_html += '<tbody>'

        milepost_html += '<tr><td>' + '</td><td>'.join(milepost_data_row) + '</td></tr>'

    if row_number > 1:
        milepost_html += '</tbody>'

# 4. Write index.html
with open(dist_dir + 'index.html', 'w') as file:
    file.write(index_html % milepost_html)
