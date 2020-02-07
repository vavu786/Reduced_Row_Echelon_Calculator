var rows = null;
var columns = null;

function addFields() {
    rows = document.getElementById("nrows").value;
    columns = document.getElementById("ncolumns").value;
    deleteElements("myTable")
    deleteElements("RRE_Output");
    deleteElements("RRE_Calc");
    deleteElements("next_line");
    var table = document.createElement("TABLE");
    table.setAttribute("id", "myTable");
    document.body.appendChild(table);
    for (i=0;i<rows;i++){
        row = table.insertRow(i);
        for (j=0;j<columns;j++){
            var cell = row.insertCell(j);
            var input = document.createElement("input");
            input.type = "text"
            cell.appendChild(input)
            cell.appendChild(document.createElement("br"));
        }
    }
    button = document.createElement("BUTTON")
    button.setAttribute("id", "RRE_Calc");
    button.setAttribute("onClick", "getFields();");
    button.innerHTML = "Perform Reduced Row Echelon Calculation";
    document.body.appendChild(button);
}

function deleteElements(id) {
    var container = document.getElementById(id);
    if (container != null) {
        document.body.removeChild(container);
    }
} 
function getFields() {
    var table_values = [];
    var table = document.getElementById("myTable");
    var num_rows = table.rows.length
    var num_cols = table.columns.length
    var table_values = ""
    for (i=0;i<num_rows;i++){
        for (j=0;j<num_cols;j++){
            var row = table.rows[i];
            var cell = row.childNodes[j].children[0].value;
            table_values = table_values + cell + " ";
        }
    }
    runCalculation(rows, columns, table_values, show_equations)
}

function runCalculation(rows, columns, values, show_equations)
{
  deleteElements("RRE_Output");
  deleteElements("next_line");
  $.getJSON('run-rre-calculation', { "Rows": rows, "Columns": columns, "MatrixValues": values, "Show_equations": show_equations}, function(data) {
      console.log(values);
      console.log(data.info);

      next_line = document.createElement("br");
      next_line.setAttribute("id", "next_line");
      document.body.appendChild(next_line);

      ele = document.createElement("TEXTAREA");
      ele.setAttribute("id", "RRE_Output");
      ele.innerHTML = data.info.RRE;
      ele.readOnly = true;
      document.body.appendChild(ele);
  });
}
