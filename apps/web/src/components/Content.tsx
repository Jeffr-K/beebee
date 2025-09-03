import styled from '@emotion/styled';

const ContentContainer = styled.main`
  flex: 1;
  padding: 2rem;
  background-color: white;
`;

const Container = styled.div`
  max-width: 1200px;
  margin: 0 auto;
`;

const Title = styled.h1`
  font-size: 2rem;
  font-weight: bold;
  color: #1e293b;
  margin-bottom: 1rem;
`;

const Description = styled.p`
  font-size: 1.125rem;
  color: #64748b;
  line-height: 1.6;
  margin-bottom: 2rem;
`;

const Card = styled.div`
  background-color: #f8fafc;
  padding: 1.5rem;
  border-radius: 0.5rem;
  border: 1px solid #e2e8f0;
  margin-bottom: 1rem;
`;

const CardTitle = styled.h2`
  font-size: 1.25rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.5rem;
`;

const CardText = styled.p`
  color: #64748b;
  line-height: 1.5;
`;

const Content = () => {
  return (
    <ContentContainer>
      <Container>
        <Title>Welcome to My App</Title>
        <Description>
          This is the main content area of your application. Here you can display your app's content, forms, data, and more.
        </Description>
        
        <Card>
          <CardTitle>Getting Started</CardTitle>
          <CardText>
            This layout includes a header, sidebar, main content area, and footer. You can customize each component to match your design requirements.
          </CardText>
        </Card>
        
        <Card>
          <CardTitle>Features</CardTitle>
          <CardText>
            • Responsive design with CSS styling<br/>
            • Modular component structure<br/>
            • Easy to customize and extend<br/>
            • Clean and modern UI
          </CardText>
        </Card>
      </Container>
    </ContentContainer>
  );
};

export default Content; 