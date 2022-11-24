# fluxcoin secure ledger
# Jxcob-Vfx (c) 2022

# this is a secure ledger that tracks and publicly displays the transactions made on the fluxcoin blockchain

# import data libraries
import os, time, datetime
from datetime import datetime
# set admin access boolean to false by default
ADMIN_VERIFIED = False

# this entire script is broken up into a series of subroutines that are mostly called by the main function and its subsidiaries

def clearError():
  # error when end user does not want to clear ledger
  os.system("clear")
  print("\033[1mINVALID INPUT\033[0m"); print(); print("Ledger will not be cleared."); print()
  e = str(input("Press enter to continue "))
  __init__()
  
def adminError():
  # menu error while admin user is trying to access an admin panel
  os.system("clear")
  print("\033[1mADMIN ERROR\033[0m"); print()
  print("Unknown error while trying to access admin privileges."); print()
  print("Most likely invalid input in an admin-only menu."); print()
  e = str(input("Press enter to continue "))
  __init__()
  
def comingSoon():
  # error telling end user that a feature is coming soon
  os.system("clear")
  print("\033[1mCOMING SOON\033[0m"); print(); print("This feature has not yet been added."); print();
  e = str(input("Press enter to continue "))
  __init__()
  
def error():
  # general error when end user input is invalid
  os.system("clear")
  print("\033[1mERROR\033[0m"); print()
  print("Unknown error - most likely invalid input."); print()
  e = str(input("Press enter to continue "))
  __init__()

def viewWallet():
  # script for end user to see the balance of any other user
  os.system("clear")
  print("\033[1mVIEW WALLET\033[0m"); print()
  walletToView = str(input("User wallet to view > ")); print()
  try:
    # read user balance
    # note that this code is nested within "try" in case there is a handling error or the user file doesn't exist
    user = open(f"{walletToView}.txt", "r"); userBalance = str(user.read()); user.close()
    print(f"User {walletToView} has a balance of {userBalance} FLX"); print()
    convUSD = int(userBalance) / 10000
    convUSD = round(convUSD, 2)
    print(f"{userBalance} FLX is equal to $ {convUSD} USD"); print()
    f = str(input("Press enter to return to main menu "))
    __init__()
  except:
    os.system("clear")
    print("\033[1mERROR\033[0m"); print(); print("Invalid user/wallet ID."); print()
    e = str(input("Press enter to return to main menu "))
    __init__()
    
def viewActiveBlock():
  # show admin user the active block for read/write
  # the active block is used to identify different groups of transactions and it is added next to them on the ledger
  os.system("clear")
  f = open("activeblock.txt", "r")
  viewActiveBlockVar = str(f.read())
  f.close()
  print(f"Active block: {viewActiveBlockVar}"); print()
  time.sleep(2); adminMode()

def viewSecurityKey():
  # show admine user the active security key
  # similar to the block, this key is a stylistic choice that can assist in differentiating between groups of transactions
  os.system("clear")
  f = open("securitykey.txt", "r")
  viewSecurityKeyVar = str(f.read())
  f.close()
  print(f"Security key: {viewSecurityKeyVar}"); print()
  time.sleep(2); adminMode()

def modifyActiveBlock():
  # use write mode to allow admin user to wipe and rename the active block
  os.system("clear")
  f = open("activeblock.txt", "w")
  print("\033[1mMODIFY ACTIVE BLOCK\033[0m"); print()
  newBlock = str(input("New block to read/write from > "))
  f.write(str(newBlock))
  f.close()
  os.system("clear")
  print("\033[1mOPERATION SUCCESSFUL\033[0m"); print(); print(f"Reading/writing from {newBlock}"); print()
  time.sleep(2); adminMode()

def modifySecurityKey():
  # use write mode to allow admin user to wipe and rename the active security key
  os.system("clear")
  f = open("securitykey.txt", "w")
  print("\033[1mMODIFY SECURITY KeY\033[0m"); print()
  newKey = str(input("New transaction security key > "))
  f.write(str(newKey))
  f.close()
  os.system("clear")
  print("\033[1mOPERATION SUCCESSFUL\033[0m"); print()
  print(f"Encrypting with key: {newKey}"); print()
  time.sleep(2); adminMode()

def adminMode():
  # admin menu
  # change the admin access boolean to \true\
  global ADMIN_VERIFIED; ADMIN_VERIFIED = True
  os.system("clear")
  print("\033[1mFLUXCOIN ADMIN\033[0m"); print()
  print("1. View active block"); print("2. Modify active block"); print("3. View security key"); print("4. Modify security key"); print("5. Exit admin console"); print()
  adminInput = input(str("> "))
  if adminInput == str("1") or adminInput == str("1."):
    viewActiveBlock()
  elif adminInput == str("2") or adminInput == str("2."):
    modifyActiveBlock()
  elif adminInput == str("3") or adminInput == str("3."):
    viewSecurityKey()
  elif adminInput == str("4") or adminInput == str("4."):
    modifySecurityKey()
  elif adminInput == str("5") or adminInput == str("5."):
    __init__()
  else:
    adminError()
def bTransfer():
  # script to transfer funds in FLX from one user to another and log them on the blockchain ledger
  os.system("clear")
  print("\033[1mBLOCKCHAIN TRANSFER\033[0m"); print()
  user1 = str(input("Wallet/user to transfer from > ")); print()
  user2 = str(input("Wallet/user to transfer to > ")); print()
  amount = int(input("Transfer amount (FLX) > ")); print()
  try:
    # again, we need a try script so that there aren't problems if we try to read a user balance file that doesn't exist
    userA = open(f"{user1}.txt", "r"); userAbalance = int(userA.read()); userA.close()
    userB = open(f"{user2}.txt", "r"); userBbalance = int(userB.read()); userB.close()
    # make sure transferring user's balance is sufficient
    if userAbalance < amount:
      print(f"Error - requested to transfer more funds than present in user wallet {user1}"); print()
      print(f"Requested: {amount}"); print(); print(f"Available: {userAbalance}"); print()
      g = str(input("Press enter to return to main menu "))
      __init__()
    else:
      # modify user balances by ofsetting the transfer amount
      newUserAbalance = userAbalance - amount
      newUserBbalance = userBbalance + amount
      changeA = open(f"{user1}.txt", "w"); changeA.write(str(newUserAbalance)); changeA.close()
      changeB = open(f"{user2}.txt", "w"); changeB.write(str(newUserBbalance)); changeB.close()
      # print transfer details to end user
      os.system("clear"); print("\033[1mTRANSFER DETAILS\033[0m"); print()
      aUSD = newUserAbalance / 10000
      bUSD = newUserBbalance / 10000
      # append transaction details to the ledger
      # fetch the date and exact time of the transaction
      now = datetime.now()
      date = now.strftime("%d/%m/%Y %H:%M:%S")
      # fetch the active security key
      key = open("securitykey.txt", "r"); sKey = str(key.read()); key.close()
      # fetch the active block
      s = open("activeblock.txt", "r"); block = str(s.read()); s.close()
      # append transfer under variable \"token"\
      token = str(f"Transferred {amount} FLX from {user1} to {user1} on block {block} | {date} | {block}/{sKey}\n")
      l = open("ledger.txt", "a"); l.write(str(token))
      # print more details to end user below heading (\;print()\)
      print(f"Transfer of {amount} FLX from {user1} to {user2} was successful"); print()
      print(f"Updated {user1} balance: {newUserAbalance} FLX")
      print(f"This is equal to $ {aUSD} USD"); print()
      print(f"Updated {user2} balance: {newUserBbalance} FLX")
      print(f"This is equal to $ {bUSD} USD"); print()
      m = str(input("Press enter to return to main menu "))
      __init__()
  except:
    # this is the except for that try loop, just in case the user file doesn't exist
    os.system("clear")
    print("\033[1mERROR\033[0m"); print(); print("One or more users not found"); print(); print(f"{user1}, {user2}"); print()
    e = str(input("Press enter to return to main menu "))
    __init__()

def balError():
  # error for when user enters a balance redemption key that doesn't exist
  # this error will always be presented to the end user for the time being; this redemption key system has not been implemented yet.
  os.system("clear")
  print("\033[1mERROR\033[0m"); print()
  print("FLX Redemption key not found"); print()
  e = str(input("Press enter to return to main menu "))
  __init__()

def create():
  # code to create a new user file on the blockchain
  os.system("clear")
  print("\033[1mCREATE WALLET\033[0m"); print()
  newWal = str(input("New wallet ID > ")); print()
  existingBalance = str(input("Does this wallet have existing balance? y or n > ")); print()
  if existingBalance == str("y") or existingBalance == str("Y"):
    bal = str(input("Enter this wallet's FLX redemption key > ")); print()
    # in the future, admins will be able to set a specific balace value for new accounts and modify existing ones. This feature has not been implemented yet.
    if bal == str("ADMIN"):
      pass
      __init__()
    else:
      balError()
  elif existingBalance == str("n") or existingBalance == str("N"):
    os.system("clear")
    a = open("activeblock.txt", "r"); activeBlock = str(a.read()); a.close()
    b = open("securitykey.txt", "r"); securityKey = str(b.read()); b.close()
    # print details (and stylistic information) to end user
    print("\033[1mOPERATION SUCCESSFUL\033[0m"); print()
    print(f"Wallet {newWal} created on block {activeBlock}"); print()
    print(f"Security key: {securityKey}"); print()
    # create new user file with a+ so that if the file already exists, the program won't crash.
    newUser = open(f"{newWal}.txt", "a+")
    newUser.write(str("0"))
    newUser.close()
    e = str(input("Press enter to return to main menu "))
    __init__()
  else:
    error()

def transaction():
  # simple menu allowing end user to abort blockchain transfer
  os.system("clear")
  print("\033[1mWRITING BLOCKCHAIN TRANSACTION\033[0m"); print()
  print("1. Blockchain transfer"); print("2. Abort"); print()
  transactionInput = str(input("> "))
  if transactionInput == str("1") or transactionInput == str("1."):
    # if user is sure, run the blockchain transfer \bTransfer()\ protocol subroutine
    bTransfer()
  elif transactionInput == str("2") or transactionInput == str("2."):
    __init__
  else:
    adminError()
def write():
  # general section / menu for modifying ledger / blockchain
  os.system("clear")
  if ADMIN_VERIFIED == True:
    # menu
    print("\033[1mWRITE TO LEDGER (ADMIN)\033[0m"); print()
    print("1. Write message to ledger"); print("2. Write transaction to ledger"); print("3. Clear ledger"); print("4. Replace ledger"); print()
    writeInput = str(input("> "))
    # write plain text message to ledger, useful for categorization
    if writeInput == str("1") or writeInput == str("1."):
      os.system("clear")
      print("\033[1mWRITING MESSAGE TO LEDGER\033[0m"); print()
      message = str(input("Message > ")); print()
      f = open("ledger.txt", "a"); f.write(str(f"{message}\n")); f.close()
      print("Message written to blockchain."); print()
      time.sleep(2); __init__()
      # since we don't want a massive chunk of code here, run the tranaction menu subroutine if user selects to make a FLX transfer
    elif writeInput == str("2") or writeInput == str("2."):
      transaction()
      # clear the entire blockchain by writing \str()\ to it
    elif writeInput == str("3") or writeInput == str("3."):
      os.system("clear")
      print("\033[1mARE YOU SURE?\033[0m"); print()
      print("You are about to permanently clear a blockchain."); print(); print("This cannot be undone."); print()
      cont = str(input("Type 'clear blockchain ledger' to continue > ")); print()
      if cont == str("clear blockchain ledger"):
        clr = open("ledger.txt", "w"); clr.write(str()); clr.close()
        os.system("clear")
        print("\033[1mOPERATION SUCCESSFUL\033[0m"); print(); print("Returning to main menu..."); print()
        time.sleep(2); __init__()
      else:
        clearError()
        # replace the existing ledger with a file added by admin user
    elif writeInput == str("4") or writeInput == str("4."):
      os.system("clear")
      print("\033[1mREPLACE LEDGER\033[0m"); print()
      replace = str(input("Filename to replace ledger with (.txt) > ")); print()
      try:
        # try and except in case specified file doesn't exist
        rep = open(f"{replace}", "r"); newLedger = str(rep.read()); rep.close()
        ledg = open("ledger.txt", "w"); ledg.write(str(newLedger)); ledg.close()
        print("Operation successful"); print(); print("Returning to main menu..."); print()
        time.sleep(2); __init__()
      except:
        # error if replacement ledger file doesn't exist
        os.system("clear")
        print("\033[1mFILENAME ERROR\033[0m"); print(); print(f"File {replace} not found"); print();
        h = str(input("Press enter to return to main menu "))
        __init__()
    else:
      adminError()
  else:
    # non-admin modification if \ADMIN_VERIFIED\ boolean = \false\
    print("\033[1mACCESS DENIED\033[0m"); print(); print("Only admins can modify the Fluxcoin ledger."); print()
    i = str(input("Press enter to continue "))
    __init__()
    
def viewLedger():
  # print active ledger
  # it's a text file and there are newline characters between every transaction, so this is quite easy to do
  os.system("clear")
  print("\033[1mFLUXCOIN LEDGER\033[0m"); print()
  f = open("ledger.txt", "r"); ledger = str(f.read()); print(ledger); f.close()
  viewInput = str(input("Press enter to return to main menu ")); __init__()
def __init__():
  # main function of the ledger
  global ADMIN_VERIFIED
  os.system("clear")
  print("\033[1mFLUXCOIN SECURE LEDGER\033[0m"); print()
  # print a message to confirm verification for admin user
  if ADMIN_VERIFIED == True:
    print("\033[1mADMIN\033[0m Verified"); print()
  else:
    pass
    # main menu
  print("1. View ledger")
  print("2. View wallet")
  print("3. Write to ledger")
  print("4. Create wallet"); print()
  mainInput = str(input("> "))
  # run existing subroutines based on end user input analysis
  # note the acceptance of \str("x")\ and \str("x.")\ in case the user is unsure
  if mainInput == str("1") or mainInput == str("1."):
    viewLedger()
  elif mainInput == str("2") or mainInput == str("2."):
    viewWallet()
  elif mainInput == str("3") or mainInput == str("3."):
    write()
  elif mainInput == str("4") or mainInput == str("4."):
    create()
  elif mainInput == str("admin"):
    adminMode()
  else:
    error()


# run main function subroutine
while True:
  __init__()
