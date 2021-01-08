
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import argparse
import time
import webbrowser

london_met_weblearn_site="https://student.londonmet.ac.uk/weblearn/"
modules_name_dict = {}
html_file=''
error_log=''

def fill(xPath, driver, filling):
	# fill the element with the filling 
	element_to_fill= driver.find_element_by_xpath( xPath )
	element_to_fill.click()
	element_to_fill.send_keys(filling)

def click(xPath, driver):
	# click the element
	element_to_press= driver.find_element_by_xpath( xPath )
	element_to_press.click()

def add_hyperlink(name, url="#"):
	# add hyperlink to the html central structure
    text = f"""
            <p>		 
                <a href=\"{url}\">{name}
                </a>
            </p>"""
    return text

def add_title(name):
	# add a section in h2 size html
    text = f"""
            <h2>{name}: 
                
            </h2>"""
    return text

def save_html(html_file):
	# save the html file
    final = f'''
            <html>
                <head>
                    <title>"London Met Scraper"</title>
                </head>
                <body bgcolor=#C2FCFC>
                {html_file}
                </body>
        </html>'''

    with open('LondonMet.html', "w") as f:
        f.write(final)

def module_loader():
	# load the module list 
		time.sleep(1)

		module_list = driver.find_elements_by_xpath("//a[@target='_top']")
		for module in module_list:

			try:
				# Check if they are really module 
				test = int(module.text[2]) 
				mname = module.text
				
				module_name_partial= driver.find_element_by_partial_link_text(mname)
				module_name_href = module_name_partial.get_attribute('href')
				modules_name_dict[mname]=module_name_href
				
			except :
				pass

def print_modules(html_file,error_log):

	print ("\n############################## Student Modules #######################################\n")

	# Add the title to the html file
	html_file+= add_title("Student Modules")

	# print the modules to the user adn update the html
	for module in modules_name_dict: 
		html_file += add_hyperlink(module,modules_name_dict[module])
		print (module)

	# Search for learning material
	for module in modules_name_dict:
		driver.execute_script("window.open('"+ modules_name_dict[module]+"', '_blank')")
		# selenium select new tab
		driver.switch_to.window(driver.window_handles[-1])

		try:
			# search partial link with the learning name
			learning_link= driver.find_element_by_partial_link_text("Learning")
			# click the larning link
			learning_link.click()

			# Check elements inside the learning material
			element_list = driver.find_elements_by_xpath('//div[@class="item clearfix"]')

			# Print all the elements

			# print title ( with module name)
			print ("\n\n" + "#" * 85)
			print (f"\n{module}\n ")		
			print ( "#" * 85 + "\n")

			# add title to html file
			html_file+= add_title(module)

			# print Elements inside Learning material
			for element in element_list:			

				try:
					link_from_parzial= driver.find_element_by_partial_link_text(element.text)
					href_partial = link_from_parzial.get_attribute('href')

					print(element.text)
					html_file+= add_hyperlink(element.text,href_partial)

					print ( "-" * 85)

				except Exception as error :
					# Error traceback no link found
					error_log +=("\n" + str(error))
					pass
		except:
			print ( "No module Learning found")
			pass				

	# print all the occurrent errors
	print ("\n\n" + "#" * 85)		
	print ("\n################################## Error Log ########################################\n")
	print ( "#" * 85)
	# print error
	print (error_log)
	# Save html file data
	save_html(html_file)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='London Metropolitan Weblearn Scaper')
	parser.add_argument('-u', '--user', help= 'Londonmet user', required=True)
	parser.add_argument('-p', '--password',  help='Londonmet password', required=True)
	
	args = parser.parse_args()

	print ('\n...Application Started...')

	options = Options()
	options.add_argument("--headless")
	driver = webdriver.Firefox(options=options)
	driver.get(london_met_weblearn_site)
	driver.implicitly_wait( 5 )
	# Web learn login
	click("/html/body/div[1]/div/div/div[3]/div[1]/div[3]/p[2]/a", driver)
	# Fill user name
	fill('//*[@id="username"]', driver, args.user )
	# Fill pwd
	fill('//*[@id="password"]', driver, args.password )
	# Press submit btn
	click('//*[@id="submit"]', driver)
	
	time.sleep(1)
	# Press on a free button Condition

	# Check if user and password are correct
	try:
		click('//*[@id="agree_button"]', driver)
	except:
		print ("\nWrong username or password\n")
		exit()
		
	# Load the modules
	module_loader()
	# print modules
	print_modules(html_file,error_log)
	# close driver
	driver.quit()
	# load html with normail firefox
	webbrowser.open('LondonMet.html')

