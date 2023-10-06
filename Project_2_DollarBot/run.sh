pip3 install -r requirements.txt

api_token=$(grep "api_token" user.properties|cut -d'=' -f2)

echo "Checking for API Token..."
if [ -z "$api_token" ]
then
  echo "Oh no! Looks like you're missing an API token. No worries."
  echo "Execute the following steps to generate the API token. Then, proceed to enter the generated token when prompted to run DollarBot."
  echo
  echo "1. Download and install the Telegram desktop application for your system from the following site: https://desktop.telegram.org/"
  echo "2. Once you login to your Telegram account, search for \"BotFather\" in Telegram. Click on \"Start\" --> enter the following command:"
  echo "/newbot"
  echo "3. Follow the instructions on screen and choose a name for your bot. Post this, select a username for your bot that ends with \"bot\" (as per the instructions on your Telegram screen)"
  echo "4. BotFather will now confirm the creation of your bot and provide a TOKEN to access the HTTP API - copy this token."
  echo
  echo "Do you want to add your API token now? (Y/n)"
  read option
  if [ $option == 'y' -o $option == 'Y' ]
  then
    echo "Enter the copied token: "
    read api_token
    echo "api_token="$api_token >> user.properties
  fi
fi

if [ -n "$api_token" ]
then
  python3 code/code.py
fi