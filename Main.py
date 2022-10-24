from Driver import Driver

def main():
    driver = Driver()
    driver.build()
    driver.get_holidays()
    driver.copy_to_clipboard()
    print('Successfully fetched the national days for today')

main()
