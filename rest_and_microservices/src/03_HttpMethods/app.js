// File 03_HttpMethods/app.js
// 
const express = require("express");
const app = express();

function printReqSummary(request) {
  console.log(`Handling ${request.method} ${request.originalUrl}`);
}

/* Store items collection in this array */
let items = [];

/* GET / -- Show main page */
app.get("/", function(request, response) {
  printReqSummary(request);
  response.send(
    `<h1>HTTP Methods</h1><ul>
      <li>Show items (GET /item)</li>
      <li>Add an item (PUT /item/:name)</li>
      <li>Remove an item (DELETE /item/:name)</li></ul>`
  );
});

/* GET /item -- Show all items from the collection */
app.get("/item", function(request, response) {
  printReqSummary(request);
  response.send(`<p>Available items: ${items.toString()}</p>`);
});

// adding new item
app.post("/item/", function(request, response) {
  printReqSummary(request);
  const name = request.query.name !== null ? request.query.name : "undefined";
  /* Is the item in collection? */
  if (items.includes(name)) {
    response.send(`<p>Item "${name}" already in collection</p>`);
  } else {
    items.push(name);
    response.send(`<p>Item "${name}" added successfully</p>`);
  }
});

// modification of an item
app.put("/item/:name", function(request, response) {
  printReqSummary(request);
  const itemName = request.params.name;
  const newItemName = request.query.newItemName !== null ? request.query.newItemName : "undefined";
  /* Is the item in collection? */
  if (items.includes(itemName)) {
    items[items.indexOf(itemName)] = newItemName;
    response.send(`<p>Item "${itemName}" changed to "${newItemName}" successfully</p>`);
  } else {
    response.send(`<p>Item "${itemName}" not found</p>`);
  }
});

/* DELETE /item/:name -- remove a given item from the collection */
app.delete("/item/:name", function(request, response) {
  printReqSummary(request);
  const itemName = request.params.name;
  /* Is the item in collection? */
  if (items.includes(itemName)) {
    items = items.filter(item => item !== itemName);
    response.send(`<p>Item "${itemName}" removed successfully</p>`);
  } else {
    response.send(`<p>Item "${itemName}" doesn't exists</p>`);
  }
});

app.listen(3000);
