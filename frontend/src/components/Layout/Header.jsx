import React from "react";
import {
  BiLock,
  BiLockOpenAlt,
  BiSearch,
  BiSolidDashboard,
  BiUser,
  BiUserCircle,
  BiWindowClose,
} from "react-icons/bi";
import { NavLink } from "react-router-dom";

import logo from "../../assets/imgs/logo.jpg";
import { useAuth } from "../../contexts/userContext";
import clsx from "clsx";

const Header = () => {
  const { isLoggedIn, setIsLoggedIn, isSearching, setIsSearching } = useAuth();
  return (
    <header className="bg-white shadow-md h-[5rem] overflow-y-hidden sticky top-0 z-50 grid items-center">
      <div className="container mx-auto py-3 flex justify-between items-center">
        <div className="flex items-center">
          <NavLink
            onClick={() => setIsSearching(false)}
            to="/"
            className="text-xl font-bold text-green-600 rounded-lg border-2 border-green-600 px-2.5 py-1.5"
          >
            {/* <img src={logo} alt="" className="h- w-64" /> */}
            RecipeHaven
          </NavLink>
        </div>
        <div className="relative group flex items-center w-[40%]">
          <input
            type="text"
            className={clsx(
              "w-full px-4 py-2 border rounded-lg",
              isSearching &&
                "focus:outline-none focus:ring-2 focus:ring-green-400"
            )}
            placeholder="Search..."
            onClick={() => setIsSearching(true)}
          />
          {!isSearching ? (
            <BiSearch
              onClick={() => setIsSearching(true)}
              className="absolute z-20 right-4 text-2xl group-hover:text-green-600 cursor-pointer"
            />
          ) : (
            <span
              onClick={() => setIsSearching(false)}
              className="absolute z-20 right-4 text-xl group-hover:text-red-600 cursor-pointer"
            >
              ❌
            </span>
          )}
        </div>
        <nav className="flex items-center space-x-4 [&_a]:font-semibold">
          <NavLink
            onClick={() => setIsSearching(false)}
            to="/recipes"
            className={({ isActive }) =>
              isActive ? "nav-link-active" : "nav-link"
            }
          >
            Recipes
          </NavLink>
          <NavLink
            onClick={() => setIsSearching(false)}
            to="/cooking_tips"
            className={({ isActive }) =>
              isActive ? "nav-link-active" : "nav-link"
            }
          >
            Cooking Tips
          </NavLink>
          {isLoggedIn ? (
            <>
              <NavLink
                onClick={() => setIsSearching(false)}
                to="/dashboard"
                className={({ isActive }) =>
                  isActive ? "nav-link-active" : "nav-link"
                }
              >
                <BiSolidDashboard className="inline-block mr-1" />
                Dashboard
              </NavLink>
              <NavLink
                onClick={() => setIsSearching(false)}
                to="/profile"
                className={({ isActive }) =>
                  isActive
                    ? "nav-link-active flex items-center justify-center"
                    : "nav-link "
                }
              >
                <BiUserCircle className="inline-block mr-1 text-2xl" />
                <span>Profile</span>
              </NavLink>
            </>
          ) : (
            <>
              <NavLink
                onClick={() => setIsSearching(false)}
                to="/about_us"
                className={({ isActive }) =>
                  isActive ? "nav-link-active" : "nav-link"
                }
              >
                About Us
              </NavLink>
              <NavLink
                onClick={() => setIsSearching(false)}
                to="/contact_us"
                className={({ isActive }) =>
                  isActive ? "nav-link-active" : "nav-link"
                }
              >
                Contact Us
              </NavLink>
            </>
          )}
          <NavLink
            onClick={() => setIsSearching(false)}
            to={isLoggedIn ? "/" : "/auth/login"}
            className={({ isActive }) =>
              isActive
                ? "flex group items-center justify-center space-x-2 text-gray-800 border border-green-600 px-4 py-1.5 rounded-2xl"
                : "flex group items-center justify-center space-x-2 text-gray-800 hover:text-gray-600 border border-cyan-300 hover:border-green-600 duration-300 ease-in-out px-4 py-1.5 rounded-2xl"
            }
            onClick={() => setIsLoggedIn(!isLoggedIn)}
          >
            <span>{isLoggedIn ? "Logout" : "Login"}</span>
            <BiLock className="group-hover:hidden" />
            <BiLockOpenAlt className="hidden group-hover:flex" />
          </NavLink>
        </nav>
      </div>
    </header>
  );
};

export default Header;
