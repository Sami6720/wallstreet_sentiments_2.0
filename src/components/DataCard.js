import { Card } from '@mui/material'
import React from 'react'


function DataCard(props) {

    const { name } = props;
  return (
    <Card>{name}</Card>
  )
}

export default DataCard