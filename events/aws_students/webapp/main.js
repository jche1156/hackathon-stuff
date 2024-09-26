
import './style.css'
import { BedrockRuntimeClient, ConverseCommand } from "@aws-sdk/client-bedrock-runtime";

const modelId = 'anthropic.claude-3-haiku-20240307-v1:0';
const prompt = "Describe a delicious item that hackathons should serve instead of pizza. `Don't show the prompt, only the dish. Do not add anything like Here is a dish. Just return the dish name alone";
const conversation = [
  {
    role: "user",
    content: [{ text: prompt }],
  },
];

async function fetchNewAffirmation() {
  disableButton(true);
  showLoadingAnimation();

  try {
    const response = await client.send(new ConverseCommand({ modelId, messages: conversation }));
    const affirmation = response.output.message.content[0].text;
    // set the affirmation in HTML
    document.querySelector("#affirmation").innerHTML = affirmation;
  } catch (err) {
    console.error(err);
    document.querySelector("#affirmation").innerHTML = err;
  }

  disableButton(false);
}

// Shows a loading animation while fetching a new affirmation
function showLoadingAnimation() {
  document.querySelector("#affirmation").innerHTML = '<div class="loading-spinner"></div>';
}

// Disables the button while fetching a new affirmation so we don't request several at once by clicking repeatedly
function disableButton(isDisabled) {
  const affirmationButton = document.querySelector("#getNewAffirmation");
  affirmationButton.disabled = isDisabled;
}

init();

// Called on page load (or refresh), fetches a new affirmation
async function init() {
  try {
    // get the user's credentials from environment variables
    const creds = await fetchCredentials();
    // instantiate the BedrockRuntimeClient  
    client = await createBedrockClient(creds);
    // Once everything is setup, let's get the first affirmation
    await fetchNewAffirmation();

  } catch(err) {
    console.error(err);
    document.querySelector("#affirmation").innerHTML = err;
  }
  
  const affirmationButton = document.querySelector("#getNewAffirmation");
  affirmationButton.addEventListener("click", fetchNewAffirmation);
}

let client = null;
async function createBedrockClient(creds) {  
  client = await new BedrockRuntimeClient({
    credentials: creds.credentials,
    region: creds.region
  });
  return client;
}

async function fetchCredentials() {
  return {
    region: "us-west-2",  // Hardcoded as this region is a requirement for the hosted Workshops and must not be changed.
    credentials: {
      accessKeyId: import.meta.env.VITE_AWS_ACCESS_KEY_ID,
      secretAccessKey: import.meta.env.VITE_AWS_SECRET_ACCESS_KEY,
      sessionToken: import.meta.env.VITE_AWS_SESSION_TOKEN,
    },
  };
}
