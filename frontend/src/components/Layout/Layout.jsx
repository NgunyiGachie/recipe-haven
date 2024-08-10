import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import Search from "./Search";

function Layout({ children }) {
  return (
    <>
      <Header />
      <Search />
      <main>{children}</main>
      <Footer />
    </>
  );
}

export default Layout;
