
# first we nee to get to the root directory so we use cd to move back 
cd ../../../..

# lets create a new directory 
mkdir source

# move the source folder to the opt directory 
sudo mv source opt/source

# now we need to move forward to our source directory 
cd opt/source

# lets install some tools #
sudo apt install git python3

# lets pull our demo app from github

sudo git clone https://github.com/Gbon1275/linux_admin_demo_app.git

# lets use the mv command to rename our app folder

sudo mv linux_admin_demo_app app

# lets check make ourself owner of the app folder
    # first we will check the permissions
        ls -l 
    # if they are owned by root we will change it by using
        sudo chown app <username>
    # now lets check the owner
        ls -l 
# lets see if our app was pulled properly

cat /app/readme.md
# lets pip install flask to run our app

# now we install the python library needed
sudo pip3 install flask

# now we can set up our demo app
cd app
export FLASK_APP=app
flask run

