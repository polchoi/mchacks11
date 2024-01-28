function submitExpense() {
  var name= document.getElementById("fname");
  var price= document.getElementById("fnumber");
  var cathegory = document.getElementById("fcathegory");
  /*
  fetch("http://127.0.0.1:8000/expense-records/", {
  method: "POST",
  body: JSON.stringify({
  "merchant_name": name,
  "price": price,
  "category": cathegory
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
})
  .then((response) => response.json())
  .then((json) => console.log(json));
*/
fetch('http://localhost:8000/expense-records/')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('table').getElementsByTagName('tbody')[0];
            data.forEach(item => {
                let row = tableBody.insertRow();
                let cell1 = row.insertCell(0);
                let cell2 = row.insertCell(1);
                let cell3 = row.insertCell(2);
                // More cells as needed

                cell1.innerHTML = item.merchant_name;
                cell2.innerHTML = item.price;
                cell3.innerHTML = item.category;
                // Update cells with actual data from your items
            });
        })
        .catch(error => console.error('Error:', error));
        window.location.href = 'index.html';


}
function del()  
    {  
        var mytable = document.getElementById("table");  
        var rows = mytable.rows.length;  
        for(var i = rows - 1; i > 0; i--)  
        {  
            if(mytable.rows[i].cells[0].children[0].checked)  
            {  
                mytable.deleteRow(i);  
            }  
        }  
    }  

