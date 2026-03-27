Step-1: We need to install Docker desktop

Step-2: We need to create a Dockerfile for guidelines
        1: Install the python
           We will give the python image with version
        2: We wil create a folder
        3: We will copy all the files
           at a time or one by one
        4: We will install the requirements.txt
        5: Last we will write how to run commands

Step-3: Open Docker desktop, skip email,
        If you get wsl error, 
        run below commands in CMD as Administrator

        wsl --update
        wsl --set-default-version 2
        wsl --version

Step-4: In your CMD first go to your Current Working Directory (CWD)
        docker build -t california-app .

        It will run all the commands 5-10 mins

Step-5: If image Successfully available we can check 
        in CMD type
        docker images (then we can be able to see california-app)

Step-6: docker run -p 8000:8000 california-app

Step-7: http://127.0.0.1:8000/predict?