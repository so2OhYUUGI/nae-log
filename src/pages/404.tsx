// src/pages/404.tsx
import React from 'react';
import { Container, Box, Typography, Button } from '@mui/material';
import Layout from '../components/Layout';
import { Link } from 'gatsby';
import SentimentVeryDissatisfiedIcon from '@mui/icons-material/SentimentVeryDissatisfied';

const NotFoundPage = () => {
  return (
    <Container maxWidth="sm">
      <Box
        py={10}
        display="flex"
        flexDirection="column"
        alignItems="center"
        justifyContent="center"
        bgcolor="#fef3e7" // 柔らかいオレンジ色の背景
        borderRadius="12px"
        textAlign="center"
      >
        <SentimentVeryDissatisfiedIcon style={{ fontSize: 100, color: '#ffa726' }} />
        <Typography variant="h4" component="h1" gutterBottom style={{ fontFamily: '"Comic Sans MS", cursive, sans-serif', color: '#ff7043' }}>
          Oops! Page not found.
        </Typography>
        <Typography variant="body1" gutterBottom style={{ fontSize: '1.25rem', color: '#ff7043' }}>
          ごめんなさい、探しているページが見つかりません。
        </Typography>
        <Button
          variant="contained"
          color="primary"
          component={Link}
          to="/"
          style={{
            backgroundColor: '#ff7043',
            borderRadius: '20px',
            fontWeight: 'bold',
            padding: '10px 20px',
            textTransform: 'none'
          }}
        >
          トップページに戻る
        </Button>
      </Box>
    </Container>
  );
};

export default NotFoundPage;
