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
#### Version 2.0.0
User-agent header for web scraping  
- Remove logging class

##### UserAgent.random_computer()
Randomly return an user-agent value that is used by computer

    UserAgent.random_computer()

##### UserAgent.random_phone()
Randomly return an user-agent value that is used by phone

    UserAgent.random_phone()

##### UserAgent.write_computer()
Save computer use user-agent headers data to file

    UserAgent.write_computer()

##### UserAgent.write_phone()
Save phone use user-agent headers data to file

    UserAgent.write_phone()


### block_class
#### Version 0.1.0
Module for file and directory

    Directory.iterate_files()

    File.file_exist()
    File.format_check(formats)


### url_collections
#### Version 0.1.1
Collection of url functions

    extract_images(input_file)

    download_image(url, target_path, [header=None])
    download_images(urls, target_directory, [header=None])
