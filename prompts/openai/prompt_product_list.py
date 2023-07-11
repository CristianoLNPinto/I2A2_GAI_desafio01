import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "Act as a web designer specialist. \nI need you to create a very simple web application for a e-commerce. This e-commerce is specilized on helth products and you need to create  its brand name. \nThis web application will be composed by three pages that we will develop step-by-step. \nYou will need write one file with HTML code, one file for java script code, and one file for CSS code. \nYou will use bootstrap to build a very beautfull interface. \nLet's start our developmento step-by-step. \nFirst tell me if you understand what are expect you develop."
    },
    {
      "role": "user",
      "content": ""
    },
    {
      "role": "assistant",
      "content": "Yes, I understand that I need to create a simple web application for an e-commerce specializing in health products. The application will consist of three pages, and I will need to write HTML, JavaScript, and CSS code for each page. I will also be using Bootstrap to create a visually appealing interface."
    },
    {
      "role": "user",
      "content": "Let's start developing the sign-in page.\nYou need to develop a centered component that will have the elements listed below:\nAn image for the logo of the brand;\nThe name brand that you you need to create a ficticious one;\nA text field for user name that must be required;\nA password text field that must be required;\nA button with label \"Entrar\" that will redirect to the page \"list_of_products.html\" only if the user name filled is \"cristiano\" and the password filled is \"i2a2@GAI\";\nA link element with the text \"Esqueci minha senha\" that will redirect to the page \"forgot_password.html\".\nLet's do it step-by-step"
    },
    {
      "role": "assistant",
      "content": "Sure, let's start developing the sign-in page step-by-step.\n\nFirst, create a new HTML file called \"sign_in.html\" and add the following code:\n\n```html\n<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <title>Sign In</title>\n  <link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css\">\n  <link rel=\"stylesheet\" href=\"styles.css\">\n</head>\n<body>\n  <div class=\"container\">\n    <div class=\"row justify-content-center\">\n      <div class=\"col-md-6\">\n        <div class=\"text-center\">\n          <img src=\"logo.png\" alt=\"Brand Logo\">\n          <h1>Brand Name</h1>\n        </div>\n        <form id=\"sign-in-form\">\n          <div class=\"form-group\">\n            <label for=\"username\">Username</label>\n            <input type=\"text\" class=\"form-control\" id=\"username\" required>\n          </div>\n          <div class=\"form-group\">\n            <label for=\"password\">Password</label>\n            <input type=\"password\" class=\"form-control\" id=\"password\" required>\n          </div>\n          <button type=\"submit\" class=\"btn btn-primary\">Entrar</button>\n        </form>\n        <div class=\"text-center mt-3\">\n          <a href=\"forgot_password.html\">Esqueci minha senha</a>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <script src=\"script.js\"></script>\n</body>\n</html>\n```\n\nIn this code, we have added the necessary HTML structure for the sign-in page. We have a container with a centered row and a column that contains the sign-in form. The form has two input fields for username and password, and a submit button. The link for \"Esqueci minha senha\" is also included.\n\nNext, create a new CSS file called \"styles.css\" and add the following code:\n\n```css\nbody {\n  background-color: #f8f9fa;\n}\n\n.container {\n  margin-top: 100px;\n}\n\n.text-center {\n  text-align: center;\n}\n\n.mt-3 {\n  margin-top: 1rem;\n}\n```\n\nThis CSS code adds some basic styling to the sign-in page. The background color is set to a light gray, and the container is centered on the page. The text-center and mt-3 classes are used for centering text and adding margin-top respectively.\n\nFinally, create a new JavaScript file called \"script.js\" and add the following code:\n\n```javascript\ndocument.getElementById('sign-in-form').addEventListener('submit', function(event) {\n  event.preventDefault();\n\n  var username = document.getElementById('username').value;\n  var password = document.getElementById('password').value;\n\n  if (username === 'cristiano' && password === 'i2a2@GAI') {\n    window.location.href = 'list_of_products.html';\n  } else {\n    alert('Invalid username or password');\n  }\n});\n```\n\nThis JavaScript code adds an event listener to the sign-in form's submit event. When the form is submitted, it prevents the default form submission behavior. It then retrieves the values entered in the username and password fields. If the username and password match the expected values, it redirects the user to the \"list_of_products.html\" page. Otherwise, it displays an alert with an error message.\n\nThat's it for the sign-in page! You can now open the \"sign_in.html\" file in a web browser to see the page in action."
    },
    {
      "role": "user",
      "content": "Replace the brand name with a ficticious name for an e-commerce specilized in helth products"
    },
    {
      "role": "assistant",
      "content": "Sure! Let's replace the brand name with a fictitious name for an e-commerce specialized in health products. \n\nIn the HTML code, replace the `<h1>` tag with the desired brand name. For example, let's use \"HealthyLife\":\n\n```html\n<div class=\"text-center\">\n  <img src=\"logo.png\" alt=\"Brand Logo\">\n  <h1>HealthyLife</h1>\n</div>\n```\n\nMake sure to update the brand name in the CSS and JavaScript files as well if necessary. \n\nNow, the sign-in page will display the fictitious brand name \"HealthyLife\" instead of the placeholder \"Brand Name\"."
    },
    {
      "role": "user",
      "content": "Generate a json list of 10 ficticious helthy products that the HealthyLife e-commerce will sell.\nThe format of the json must be like the format below:\n{'id':{{incremental_number}}, 'product_name': {{ficticious_product_name}}, 'unit_price': {{ficticious_unit_price}}, 'product_image':{{product_image_file_name}}}"
    },
    {
      "role": "assistant",
      "content": "Certainly! Here's an example of a JSON list of 10 fictitious healthy products for the HealthyLife e-commerce:\n\n```json\n[\n  {\n    \"id\": 1,\n    \"product_name\": \"Organic Green Tea\",\n    \"unit_price\": 9.99,\n    \"product_image\": \"green_tea.jpg\"\n  },\n  {\n    \"id\": 2,\n    \"product_name\": \"Superfood Smoothie Mix\",\n    \"unit_price\": 14.99,\n    \"product_image\": \"smoothie_mix.jpg\"\n  },\n  {\n    \"id\": 3,\n    \"product_name\": \"Vegan Protein Powder\",\n    \"unit_price\": 19.99,\n    \"product_image\": \"protein_powder.jpg\"\n  },\n  {\n    \"id\": 4,\n    \"product_name\": \"Gluten-Free Granola Bars\",\n    \"unit_price\": 7.99,\n    \"product_image\": \"granola_bars.jpg\"\n  },\n  {\n    \"id\": 5,\n    \"product_name\": \"Organic Chia Seeds\",\n    \"unit_price\": 6.99,\n    \"product_image\": \"chia_seeds.jpg\"\n  },\n  {\n    \"id\": 6,\n    \"product_name\": \"Natural Almond Butter\",\n    \"unit_price\": 12.99,\n    \"product_image\": \"almond_butter.jpg\"\n  },\n  {\n    \"id\": 7,\n    \"product_name\": \"Detox Herbal Tea\",\n    \"unit_price\": 8.99,\n    \"product_image\": \"detox_tea.jpg\"\n  },\n  {\n    \"id\": 8,\n    \"product_name\": \"Organic Quinoa\",\n    \"unit_price\": 5.99,\n    \"product_image\": \"quinoa.jpg\"\n  },\n  {\n    \"id\": 9,\n    \"product_name\": \"Plant-Based Protein Bars\",\n    \"unit_price\": 10.99,\n    \"product_image\": \"protein_bars.jpg\"\n  },\n  {\n    \"id\": 10,\n    \"product_name\": \"Natural Coconut Oil\",\n    \"unit_price\": 11.99,\n    \"product_image\": \"coconut_oil.jpg\"\n  }\n]\n```\n\nPlease note that the `product_image` values in the JSON represent the file names of the product images. You would need to have the corresponding image files in your project directory and update the image source paths accordingly in your HTML code."
    },
    {
      "role": "user",
      "content": "Using the same HTML file format of the page sign-in.\nReplace the form to generate the page product_list.html.\nBased on the list of json of products generated before.\nCreate a bootstrap grid for all the products.\nEach position of the grid must have:\nProduct image\nProduct name\nUnit Price\nProduct id"
    },
    {
      "role": "assistant",
      "content": "To generate the product list page based on the JSON list of products, we can modify the HTML file and use JavaScript to dynamically generate the product grid. Here's the updated code for the \"product_list.html\" page:\n\n```html\n<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <title>Product List</title>\n  <link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css\">\n  <link rel=\"stylesheet\" href=\"styles.css\">\n</head>\n<body>\n  <div class=\"container\">\n    <div class=\"row\">\n      <div class=\"col-md-12\">\n        <div class=\"text-center\">\n          <img src=\"logo.png\" alt=\"Brand Logo\">\n          <h1>HealthyLife</h1>\n        </div>\n        <div class=\"row\" id=\"product-grid\">\n          <!-- Product grid will be dynamically generated here -->\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <script src=\"products.js\"></script>\n  <script src=\"script.js\"></script>\n</body>\n</html>\n```\n\nIn this code, we have added an empty `<div>` with the id \"product-grid\" where the product grid will be dynamically generated.\n\nNext, create a new JavaScript file called \"products.js\" and add the following code:\n\n```javascript\nvar products = [\n  {\n    \"id\": 1,\n    \"product_name\": \"Organic Green Tea\",\n    \"unit_price\": 9.99,\n    \"product_image\": \"green_tea.jpg\"\n  },\n  // Add the remaining products from the JSON list here\n];\n\nvar productGrid = document.getElementById('product-grid');\n\nproducts.forEach(function(product) {\n  var productCard = document.createElement('div');\n  productCard.classList.add('col-md-4', 'mb-4');\n\n  var productImage = document.createElement('img');\n  productImage.src = product.product_image;\n  productImage.alt = product.product_name;\n  productImage.classList.add('img-fluid');\n\n  var productName = document.createElement('h3');\n  productName.textContent = product.product_name;\n\n  var unitPrice = document.createElement('p');\n  unitPrice.textContent = 'Unit Price: $' + product.unit_price.toFixed(2);\n\n  var productId = document.createElement('p');\n  productId.textContent = 'Product ID: ' + product.id;\n\n  productCard.appendChild(productImage);\n  productCard.appendChild(productName);\n  productCard.appendChild(unitPrice);\n  productCard.appendChild(productId);\n\n  productGrid.appendChild(productCard);\n});\n```\n\nIn this JavaScript code, we have defined the `products` array containing the JSON list of products. We then iterate over each product using the `forEach` method and dynamically create a Bootstrap card for each product. The card contains the product image, name, unit price, and ID. The card is then appended to the \"product-grid\" element.\n\nMake sure to have the corresponding product images in your project directory and update the image source paths in the JSON and JavaScript code accordingly.\n\nNow, when you open the \"product_list.html\" file in a web browser, it will dynamically generate a product grid based on the JSON list of products. Each grid position will display the product image, name, unit price, and ID."
    }
  ],
  temperature=0,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)