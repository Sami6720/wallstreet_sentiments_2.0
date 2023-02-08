import { Card, CardContent, Typography } from "@mui/material";
import React from "react";
import { DataGrid } from "@mui/x-data-grid";

function DataCard(props) {
  // the following rows and columns variables are all dummy data
  const columns = [
    // { field: "id", headerName: "Rank", width: 10, editable: false },
    {
      field: "stocks",
      headerName: "Stock",
      type: "string",
      soratble: true,
      editable: false,
      align: "center",
      flex: 0.2,
      headerAlign: "center",
    },
    {
      field: "total_compound",
      headerName: "Sentiment Score",
      type: "number",
      editable: false,
      soratble: true,
      align: "center",
      headerAlign: "center",
      flex: 0.2,
    },
    {
      field: "change",
      headerName: "Percentage Change",
      type: "number",
      editable: false,
      soratble: true,
      align: "center",
      flex: 0.2,
      headerAlign: "center",
    },
  ];

  // const rows = [
  //   { id: 1, stocks: "sami", total_compound_x: 35, change: 5 },
  //   { id: 2, stocks: "orthy", total_compound_x: 35, change: 5 },
  // ];

  const df2 = props.rows;
  const name = props.name;
  // const rows=props.rows;
  return (
    <Card>
      <CardContent sx={{ height: 400, width: "100%" }}>
        <Typography sx={{ fontSize: 14 }} color="text.primary" gutterBottom>
          {name}
        </Typography>
        <DataGrid
          rows={df2}
          columns={columns}
          pageSize={5}
          rowsPerPageOptions={[5]}
        />
      </CardContent>
    </Card>
  );
}

export default DataCard;
