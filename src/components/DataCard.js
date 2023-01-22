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
      align: "center",
      flex: 0.2,
    },
    {
      field: "Total_Compound",
      headerName: "Sentiment Score",
      type: "number",
      editable: false,
      soratble: true,
      align: "center",
      flex: 0.4,
    },
    {
      field: "Percentage_Change",
      headerName: "Change",
      type: "number",
      editable: false,
      soratble: true,
      align: "center",
      flex: 0.4,
    },
  ];

  const rows = [
    { id: 1, Stocks: "sami", Total_compund: 35, Percentage_Change: 5 },
    { id: 2, Stocks: "orthy", Total_compund: 35, Percentage_Change: 5 },
  ];

  // const rows=props.rows;
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
