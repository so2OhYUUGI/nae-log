import React from "react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import Button from "@mui/material/Button";
import axios from "axios";

const queryClient = new QueryClient();

const TestButton: React.FC = () => {
  const toggleLamp = async (state: "on" | "off") => {
    const url = `http://raspberrypi.local:8000/api/lamp/`;
    const response = await axios.post(url, { state });
    return response.data;
  };

  const handleClick = async (status: "on" | "off") => {
    try {
      await toggleLamp(status);
      //alert(`Lamp switched ${status}`);
    } catch (error) {
      console.error("Failed to switch lamp", error);
      //alert("Failed to switch lamp");
    }
  };

  return (
    <>
      <Button
        variant="contained"
        color="primary"
        onClick={() => handleClick("on")}
      >
        Turn On
      </Button>
      <Button
        variant="contained"
        color="secondary"
        onClick={() => handleClick("off")}
      >
        Turn Off
      </Button>
    </>
  );
};

export default TestButton;
