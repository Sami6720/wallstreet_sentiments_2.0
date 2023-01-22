import { Card, CardContent, Typography } from "@mui/material";
import React from "react";
import { DataGrid } from "@mui/x-data-grid";

function DataCard(props) {
  // the following rows and columns variables are all dummy data
  const columns = [
    // { field: "id", headerName: "Rank", width: 10, editable: false },
    {
      field: "Stocks",
      headerName: "Stock",
      type: "string",
      soratble: true,
      editable: false,
      headerAlign: "center",
      flex: 0.2
    },
    {
      field: "Total_Compound",
      headerName: "Sentiment Score",
      type: "number",
      editable: false,
      soratble: true,
      headerAlign: "center",
      flex: 0.4,
    },
    {
      field: "Percentage_Change",
      headerName: "Change",
      type: "number",
      editable: false,
      soratble: true,
      headerAlign: "center",
      flex: 0.4,
    },
  ];

  const rows = [
    { id: 1, lastName: "Snow", firstName: "Jon", age: 35 },
    { id: 2, lastName: "Lannister", firstName: "Cersei", age: 42 },
    { id: 3, lastName: "Lannister", firstName: "Jaime", age: 45 },
    { id: 4, lastName: "Stark", firstName: "Arya", age: 16 },
    { id: 5, lastName: "Targaryen", firstName: "Daenerys", age: null },
    { id: 6, lastName: "Melisandre", firstName: null, age: 150 },
    { id: 7, lastName: "Clifford", firstName: "Ferrara", age: 44 },
    { id: 8, lastName: "Frances", firstName: "Rossini", age: 36 },
    { id: 9, lastName: "Roxie", firstName: "Harvey", age: 65 },
  ];

  const { name } = props;
  return (
    <Card>
      <CardContent sx={{ height: 400, width: "100%" }}>
        <Typography sx={{ fontSize: 14 }} color="text.primary" gutterBottom>
          {name}
        </Typography>
        <DataGrid
          rows={rows}
          columns={columns}
          pageSize={5}
          rowsPerPageOptions={[5]}
        />
      </CardContent>
    </Card>
  );
}

export default DataCard;
