import React, { createContext, useContext, useState } from "react";

const UserContext = createContext();

export const useAuth = () => useContext(UserContext);

export const UserProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isSearching, setIsSearching] = useState(false);

  return (
    <UserContext.Provider
      value={{ isLoggedIn, setIsLoggedIn, isSearching, setIsSearching }}
    >
      {children}
    </UserContext.Provider>
  );
};
