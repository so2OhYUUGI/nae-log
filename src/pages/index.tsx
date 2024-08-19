import React from "react";
import Button from "@mui/material/Button";

const TestButton: React.FC = () => {
  return (
    <Button variant="contained" color="primary">
      Test Button
      {process.env.NAELOG_API_URL}
    </Button>
  );
};

export default TestButton;
