# Python modules
Modules use for writing python programs


### logging_class
#### Version 1.1.0
`name` set the logging file name, `directory` set logging file placement  
Logging class for use in other python programs

    PersonalLog(name, [directory])
    PersonalLog.debug(message)
    PersonalLog.info(message)
    PersonalLog.warning(message)
    PersonalLog.error(message)
    PersonalLog.critical(message)


### user_agent_class
User-agent header for web scraping  
#### Version 2.1.0
- Add firefox user-agent fetching function
- Add chrome user-agent fetching function


##### UserAgent.random_computer()
Randomly return an user-agent value that is used by computer

    UserAgent.random_computer()

##### UserAgent.random_phone()
Randomly return an user-agent value that is used by phone

    UserAgent.random_phone()

##### UserAgent.random_firefox()
Randomly return an user-agent value that is used by firefox browser

    UserAgent.random_firefox()

##### UserAgent.random_chrome()
Randomly return an user-agent value that is used by chrome browser

    UserAgent.random_chrome()

##### UserAgent.write_computer()
Save computer use user-agent headers data to file

    UserAgent.write_computer()

##### UserAgent.write_phone()
Save phone use user-agent headers data to file

    UserAgent.write_phone()

##### UserAgent.write_firefox()
Save firefox browser user-agent headers data to file

    UserAgent.write_firefox()

##### UserAgent.write_chrome()
Save chrome browser user-agent headers data to file

    UserAgent.write_chrome()


### block_class
#### Version 0.1.1
Module for file and directory

    Directory.iterate_files()

    File.file_exist()
    File.format_check(formats)


### url_collections
#### Version 0.1.3
- Add duplicates option to extract_images function

Collection of url functions

    extract_images(input_file, [duplicates=False])

    download_image(url, target_path, [header=None])
    download_images(urls, target_directory, [header=None])
