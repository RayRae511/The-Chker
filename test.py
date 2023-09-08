from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the database engine
engine = create_engine('sqlite:///expenses.db', echo=True)

# Create the base class for declarative models
Base = declarative_base()

# Define the Expense model
class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    description = Column(String)
    category = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return f"Expense(date={self.date}, description={self.description}, category={self.category}, price={self.price})"

# Create the database tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add an expense
new_expense = Expense(description='Groceries', category='Food', price=50)
session.add(new_expense)
session.commit()

# Query all expenses
expenses = session.query(Expense).all()
for expense in expenses:
    print(expense)
