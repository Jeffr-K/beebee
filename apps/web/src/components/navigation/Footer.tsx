import styled from '@emotion/styled';

const FooterContainer = styled.footer`
  background-color: #1e293b;
  color: white;
  padding: 1rem;
  text-align: center;
  margin-top: auto;
`;

const Container = styled.div`
  max-width: 1200px;
  margin: 0 auto;
`;

const Text = styled.p`
  font-size: 0.875rem;
  color: #94a3b8;
`;

const Footer = () => {
  return (
    <FooterContainer>
      <Container>
        <Text>
          © 2024 My App. All rights reserved.
        </Text>
      </Container>
    </FooterContainer>
  );
};

export default Footer; 