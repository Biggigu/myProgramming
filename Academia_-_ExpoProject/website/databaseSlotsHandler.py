import sqlite3
from datetime import datetime, timedelta

class MyDatabase:
    def connect(self):
        # Assuming you're using SQLite, adjust for your DB connection
        return sqlite3.connect('escapeRoom.db')

    def newDBIfNoExist(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS timeSlots (
                            bookingDate VARCHAR(50),
                            bookingTime VARCHAR(50),
                            username VARCHAR(50),
                            played BOOLEAN DEFAULT False);''')
        connection.commit()
        connection.close()

    def insertDefault(self, startDate, endDate, startTime, endTime):
        connection = self.connect()
        cursor = connection.cursor()
        
        # Parse startDate and endDate
        start_date = datetime.strptime(startDate, '%Y-%m-%d')
        end_date = datetime.strptime(endDate, '%Y-%m-%d')
        
        # Parse startTime and endTime
        start_time = datetime.strptime(startTime, '%H:%M')
        end_time = datetime.strptime(endTime, '%H:%M')

        # Loop through dates
        current_date = start_date
        while current_date <= end_date:
            # Loop through times
            current_time = start_time
            while current_time <= end_time:
                # Format the time slot as HH:MM
                time_slot = current_time.strftime('%H:%M')
                
                # Insert the record into the database
                cursor.execute('''INSERT INTO timeSlots (bookingDate, bookingTime, username) 
                                VALUES (?, ?, ?)''', 
                                (current_date.strftime('%Y-%m-%d'), time_slot, ''))
                
                # Move to the next time slot (30 minutes)
                current_time += timedelta(minutes=30)

            # Move to the next day
            current_date += timedelta(days=1)
        
        connection.commit()
        connection.close()

# Example usage

if __name__ == '__main__':
    db = MyDatabase()
    db.newDBIfNoExist()  # Create the table if it doesn't exist
    db.insertDefault('2025-05-21', '2025-05-27', '10:00', '12:00')  # Insert default slots
