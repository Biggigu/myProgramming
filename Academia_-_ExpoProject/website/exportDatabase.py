from flask import send_file, Blueprint
import pandas as pd
from io import BytesIO
import sqlite3

exportDB = Blueprint('export', __name__)

@exportDB.route('/export', methods=['GET'])
def exportData():
    conn = sqlite3.connect('academia.db')
    df = pd.read_sql_query("SELECT * FROM players", conn)
    conn.close()

    # Convert to Excel in memory
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Data')
    output.seek(0)

    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name='Participants_Score.xlsx'
    )
