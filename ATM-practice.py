import pandas as pd
import random
import datetime
import os

def tracker(user_name, user_id, withed_amount, added_amount, balance, date):
    df_history = pd.read_csv('ATM-history.csv')
    new = {
        'username': user_name,
        'userId': user_id,
        'takenAmount': withed_amount,
        'addedAmount': added_amount,
        'balance': balance,
        'date': date
    }
    df_new = pd.DataFrame([new])
    df_new = df_new.fillna('')
    df_history = pd.concat([df_history, df_new], ignore_index=True)
    df_history.to_csv('ATM-history.csv', index=False)

def menuOfOptions():
    print('--1. Show Balance--')
    print('--2. Make a Withdraw (service - 3%)--')
    print('--3. Make a Deposit--')
    print('--4. Change a Password--')
    print('--5. Change a Username--')
    print('--6. History of a card--')

def withdraw(df, user_id, amount):
    balance = df.loc[df['userId'] == user_id, 'balance'].values[0]
    service_charge = amount * 3 / 100
    balance = (balance - amount) - service_charge
    #можно добавить column of sum of service charges
    df.loc[df['userId'] == user_id, 'balance'] = balance
    df.to_csv('ATM-users.csv', index=False)

    print(f'You have successfully made the withdraw!\n${amount}')
    print(f'Your balance is ${balance}')
    date = datetime.datetime.now()
    formated_date = date.strftime("%Y-%m-%d %H:%M:%S")

    user_name = df.loc[df['userId'] == user_id, 'username'].values[0]
    tracker(user_name, user_id, amount, 0, balance, formated_date)

def deposit(df, user_id, amount):
    balance = df.loc[df['userId'] == user_id, 'balance'].values[0]
    balance += amount
    df.loc[df['userId'] == user_id, 'balance'] = balance
    df.to_csv('ATM-users.csv', index=False)

    print(f'You have successfully made the deposit!\n${amount}')
    print(f'Your balance is ${balance}')
    date = datetime.datetime.now()
    formated_date = date.strftime("%Y-%m-%d %H:%M:%S")

    user_name = df.loc[df['userId'] == user_id, 'username'].values[0]
    tracker(user_name,user_id, 0, amount, balance, formated_date)

def changePassword(df, user_id):
    old_password = input('Enter your old password: ')
    new_password = ''
    if old_password == df.loc[df['userId'] == user_id, 'password'].values[0]:
        new_password = input('Enter your new password: ')
        df.loc[df['userId'] == user_id, 'password'] = new_password
        df.to_csv('ATM-users.csv', index=False)
        print('Password changed successfully!')
    elif new_password == old_password:
        print('New password cannot be the same as the old one!')
    else:
        print('Incorrect password!')

def changeUsername(df, user_id):
    verification = input('Enter your password: ')
    new_username = ''
    if verification == df.loc[df['userId'] == user_id, 'password'].values[0]:
        new_username = input('Enter your new username: ')
        df.loc[df['userId'] == user_id, 'username'] = new_username
        df.to_csv('ATM-users.csv', index=False)
        print('Username changed successfully!')
    elif new_username == df.loc[df['userId'] == user_id, 'username'].values[0]:
        print('New username cannot be the same as the old one!')
    else:
        print('Incorrect password!')

def showHistory(df, user_name):
    if df.loc[df['username'] == user_name].empty:
        print(f'User - {user_name} does not have a history')
    else:
        print(f'History of user - {user_name}')
        all_data = df[df['username'] == user_name]
        all_data.index = (range(1, len(all_data) + 1))
        print(all_data)

def user_confirmation():
    while True:
        confirmation = input('Do you want to continue - Y/N - ')
        match confirmation:
            case 'Y' | 'y':
                return True
            case 'N' | 'n':
                print('Bye!')
                return False
            case _:
                print('Wrong input! It should be Y/N')

def signIn(df):
    user_name = input('Enter your username: ')

    if user_name in df['username'].values:
        password = input('Enter your password: ')
        if password == df.loc[df['username'] == user_name, 'password'].iloc[0]:
            print(f'Welcome {user_name}')

            while True:
                menuOfOptions()
                choiceOfUser = int(input('What you want ? - '))

                if choiceOfUser == 1:
                    balance = df.loc[df['username'] == user_name, 'balance'].values[0]
                    if balance.size > 0:
                        print(f'Your balance - ${balance}')
                    else:
                        print('You have no balance!\nTry again!')


                elif choiceOfUser == 2:
                    amount = float(input('Enter the amount to withdraw - '))
                    amount = round(amount, 2)
                    if amount > df.loc[df['username'] == user_name, 'balance'].values[0]:
                        print('Insufficient funds in your balance!')
                    else:
                        user_id = df.loc[df['username'] == user_name, 'userId'].values[0]
                        confirmation = int(input('Confirm your withdraw with your ID - '))
                        if user_id == confirmation:
                            Withdraw = withdraw(df, user_id=user_id, amount=amount)
                        else:
                            print('Incorrect ID!')
                            print('Try again!')


                elif choiceOfUser == 3:
                    amount = float(input('Enter the amount to deposit - '))
                    amount = round(amount, 2)
                    if amount < 0:
                        print('You cannot deposit a negative amount!')
                    else:
                        user_id = df.loc[df['username'] == user_name, 'userId'].values[0]
                        confirmation = int(input('Confirm your deposit with your ID - '))
                        if user_id == confirmation:
                            Deposit = deposit(df, user_id=user_id, amount=amount)
                        else:
                            print('Incorrect ID!')
                            print('Try again!')


                elif choiceOfUser == 4:
                    changePassword(df, user_id=df.loc[df['username'] == user_name, 'userId'].values[0])


                elif choiceOfUser == 5:
                    changeUsername(df, user_id=df.loc[df['username'] == user_name, 'userId'].values[0])


                elif choiceOfUser == 6:
                    history = pd.read_csv('ATM-history.csv')
                    showHistory(history, user_name)

                else:
                   print('Invalid Choice!')

                if not user_confirmation():
                    break
        else:
            print('Incorrect Password!')
    else:
        print(f'Account "{user_name}" does not exist!')


def signUp(df):
    user_name = input('Enter new username: ')

    if user_name in df['username'].values:
        print(f'{user_name} already exists')
    else:
        password = input('Enter new password: ')
        user_id = random.randint(1000, 9999)
        year = random.randint(2026, 2032)
        month = random.randint(1, 12)
        card_exp = f'{month}/{year}'
        balance = 0

        new_user = {
            'userId': user_id,
            'username': user_name,
            'password': password,
            'cardExp': card_exp,
            'balance': balance
        }

        new_user = pd.DataFrame([new_user])

        df = pd.concat([df, new_user], ignore_index=True)

        df.to_csv('ATM-users.csv', index=False)

        print(f"Congrats! You have successfully Signed Up...\n"
              f"Your User ID : {df.loc[df['username'] == user_name, 'userId'].values[0]}\n"
              f"Your Card Exp Date : {df.loc[df['username'] == user_name, 'cardExp'].values[0]}")

def resetPassword(df):
    user_name = input('Enter your username: ')
    verification = int(input('Enter your ID: '))
    if verification == df.loc[df['username'] == user_name, 'userId'].values[0]:
        new_password = input('Enter your new password: ')
        df.loc[df['username'] == user_name, 'password'] = new_password
        df.to_csv('ATM-users.csv', index=False)
        print('Password changed successfully!')
    else:
        print('Incorrect ID!')

def deleteAccount(df):
    user_id = int(input('Enter your id: '))
    if user_id in df['userId'].values:
        index = df[df['userId'] == user_id].index
        verification = input('Do u really wanna delete this account - Y/N - ')
        match verification:
            case 'Y' | 'y':
                df.drop(index, inplace=True)
                df.to_csv('ATM-users.csv', index=False)
                print('Account deleted successfully!')
            case 'N' | 'n':
                print('Account not deleted!')
    else:
        print('Wrong ID!')
        print('Or Account does not exist!')






if __name__ == '__main__':
    print('--1. Sign In--')
    print('--2. Sign Up--')
    print('--3. Reset Password--')
    print('--4. Delete Account--')
    choiceOfUser = int(input('What you want ? - '))


    data = pd.read_csv('ATM-users.csv')
    data['balance'] = data['balance'].astype(float)
    data['balance'] = data['balance'].round(2)
    data.to_csv('ATM-users.csv', index=False)

    if choiceOfUser == 1:
        signIn(data)
    elif choiceOfUser == 2:
        signUp(data)
    elif choiceOfUser == 3:
        resetPassword(data)
    elif choiceOfUser == 4:
        deleteAccount(data)
    else:
        print('Invalid Choice bruh!')



