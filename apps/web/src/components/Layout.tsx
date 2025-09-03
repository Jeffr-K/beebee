import styled from '@emotion/styled';
import Header from './navigation/Header';
import Sidebar from './navigation/Sidebar';
import Content from './Content';
import Footer from './navigation/Footer';

const LayoutContainer = styled.div`
  display: flex;
  flex-direction: column;
  min-height: 100vh;
`;

const MainContent = styled.div`
  display: flex;
  flex: 1;
`;

const Layout = () => {
  return (
    <LayoutContainer>
      <Header />
      <MainContent>
        <Sidebar />
        <Content />
      </MainContent>
      <Footer />
    </LayoutContainer>
  );
};

export default Layout;