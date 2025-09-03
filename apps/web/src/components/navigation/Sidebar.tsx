import styled from '@emotion/styled';

const SidebarContainer = styled.aside`
  width: 250px;
  background-color: #f8fafc;
  border-right: 1px solid #e2e8f0;
  padding: 1rem;
  min-height: calc(100vh - 140px);
`;

const Menu = styled.ul`
  list-style: none;
  padding: 0;
  margin: 0;
`;

const MenuItem = styled.li`
  margin-bottom: 0.5rem;
`;

const MenuLink = styled.a<{ $active?: boolean }>`
  display: block;
  padding: 0.75rem 1rem;
  color: ${props => props.$active ? 'white' : '#64748b'};
  text-decoration: none;
  border-radius: 0.375rem;
  transition: all 0.3s ease;
  background-color: ${props => props.$active ? '#3b82f6' : 'transparent'};
  
  &:hover {
    background-color: ${props => props.$active ? '#2563eb' : '#e2e8f0'};
    color: ${props => props.$active ? 'white' : '#1e293b'};
  }
`;

const Sidebar = () => {
  return (
    <SidebarContainer>
      <nav>
        <Menu>
          <MenuItem>
            <MenuLink href="#" $active>Dashboard</MenuLink>
          </MenuItem>
          <MenuItem>
            <MenuLink href="#">Users</MenuLink>
          </MenuItem>
          <MenuItem>
            <MenuLink href="#">Settings</MenuLink>
          </MenuItem>
          <MenuItem>
            <MenuLink href="#">Analytics</MenuLink>
          </MenuItem>
        </Menu>
      </nav>
    </SidebarContainer>
  );
};

export default Sidebar; 