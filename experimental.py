from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    # Set up ChromeDriver as specified by documentation
    driver = webdriver.Chrome()

    # Call the get info function to get the information from the text file provided
    lines = get_info()

    # Assign username and password
    username = lines[0]
    password = lines[1]
    target = lines[2]

    driver.set_page_load_timeout(10)
    driver.get(target)
    driver.find_element_by_id("identifierId").send_keys(username)
    driver.find_element_by_id("identifierNext").click()
    time.sleep(2)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("passwordNext").click()
    time.sleep(4)
    driver.find_element_by_id("yDmH0d").send_keys(Keys.TAB, Keys.ENTER)
    time.sleep(3)
    driver.find_element_by_tag_name("textarea").send_keys("hello, just testing something")

    time.sleep(1)
    upcoming_amount = len(driver.find_elements_by_class_name("hrUpcomingAssignmentGroup"))
    tab_amount = 10 + upcoming_amount
    print(upcoming_amount)
    driver.find_element_by_id("yDmH0d").send_keys(Keys.TAB * tab_amount)
    time.sleep(3)

    driver.find_element_by_id("yDmH0d").send_keys(Keys.TAB, Keys.ENTER, Keys.ARROW_DOWN * 2, Keys.ENTER)
    time.sleep(4)

    with open("imgs_to_load.txt", "r") as f:
        new_file = f.readlines()
        img_url = new_file[0].strip("\n")
        new_file.pop(0)

    new_file_stringed = ""
    for item in new_file:
        new_file_stringed += item

    with open("imgs_to_load.txt", "w") as f:
        f.write(new_file_stringed)

    # driver.find_element_by_tag_name("input").send_keys(img_url)
    # driver.find_element_by_id("yDmH0d").send_keys(Keys.TAB * 2, Keys.ENTER)
    # time.sleep(5)
    #
    # # Post the assignment and quit
    # driver.find_element_by_id("yDmH0d").send_keys(Keys.TAB * 2, Keys.ENTER)
    # driver.quit()


def get_info():
    # Grab the information for the class and assign the list returned by "readlines()" to lines
    with open("info_experimental.txt", "r+") as f:
        lines = f.readlines()
        if len(lines) < 3:
            needed = what_missing(lines)
            print(f"Missing: {item}" for item in needed)
            raise IOError()

    # Within this list strip the new line escape code (\n)
    labels = ["un: ", "pw: ", "url: "]
    for element in lines:
        current_index = lines.index(element)
        stripped = element.strip("\n")
        for label in labels:
            stripped = stripped.strip(label)
        lines[current_index] = stripped

    return lines


def what_missing(present_items):
    needed_items = ["un", "pw", "url"]
    if len(present_items) > 1:
        needed_items.remove(present_items[0])
        needed_items.remove(present_items[1])
    else:
        needed_items.remove(present_items[0])
    return needed_items


if __name__ == "__main__":
    main()
