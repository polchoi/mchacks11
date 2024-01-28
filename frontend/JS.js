function submitExpense() {
    fetch("http://127.0.0.1:8000/expense-records", {
  method: "POST",
  body: JSON.stringify({
    "username": "test",
  "merchant_name": "testtttt",
  "price": 11,
  "category": "beans"
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
})
  .then((response) => response.json())
  .then((json) => console.log(json));
}