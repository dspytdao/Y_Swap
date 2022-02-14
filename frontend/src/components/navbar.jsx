import { motion } from "framer-motion";
import React, { useState } from "react";
import { Link } from "react-router-dom";
import { HiOutlineMenu } from "react-icons/hi";
import {FiGithub} from "react-icons/fi";
const Navbar = () => {
  const [open, setOpen] = useState(false);
  const toggleMenu = () => {
    setOpen(!open);
  };
  const barVariants = {
    open: { opacity: 1 },
    closed: { opacity: 0 },
  };
  return (
    <>
      {" "}
      <nav className="bg-gradient-to-l from-gray-200 via-emerald-50 to-emerald-200 border-gray-200 px-2 sm:px-4 py-2.5 rounded shadow-lg">
        <div className="container flex flex-wrap justify-between items-center mx-auto">
          <Link
            to="/"
            className="flex self-center text-lg font-semibold whitespace-nowrap"
          >
            Algo Broker
          </Link>
          <button
            onClick={toggleMenu}
            className="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-200"
          >
            <HiOutlineMenu size="20" />
          </button>
          <div className="hidden w-full md:block md:w-auto">
            <ul className="flex flex-col mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium">
              <li>
                <Link
                  to="/"
                  className="block transition py-2 pr-4 pl-3 text-black hover:bg-blue-100 rounded md:bg-transparent md:text-blue-900 md:px-2 "
                >
                  Home
                </Link>
              </li>
              <li>
                <Link
                  to="/swap"
                  className="block transition py-2 pr-4 pl-3 text-black hover:bg-blue-100 rounded md:bg-transparent md:text-blue-900 md:px-2 "
                >
                  Swap
                </Link>
              </li>
              <li>
                <a
                  href="https://github.com/dspytdao/Y_Swap"
                  target="_blank"
                  className="block transition py-2 pr-4 pl-3 text-black hover:bg-blue-100 rounded md:bg-transparent md:text-blue-800 md:px-2  "
                >
                  <FiGithub size={20}/>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <motion.div
        animate={open ? "open" : "closed"}
        variants={barVariants}
        className={`${
          open ? "" : "hidden"
        } w-full shadow-lg mb-2 md:hidden bg-gradient-to-l from-gray-200 via-emerald-50 to-emerald-200 border-gray-200`}
      >
        <ul className="flex flex-col  md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium text-center">
          <li>
            <Link
              to="/"
              className="block transition py-2 pr-4 pl-3 text-black hover:bg-blue-400/30 rounded md:bg-transparent md:text-blue-900 md:px-2"
            >
              Home
            </Link>
          </li>
          <li>
            <Link
              to="/swap"
              className="block transition py-2 pr-4 pl-3 text-black hover:bg-blue-400/30 rounded md:bg-transparent md:text-blue-900 md:px-2"
            >
              Swap
            </Link>
          </li>
          <li>
            <a
              href="https://github.com/dspytdao/Y_Swap"
              target="_blank"
              className="block transition py-2 pr-4 pl-3 font-semibold text-black  hover:bg-blue-400/30 rounded md:bg-transparent md:text-blue-800 md:px-2"
            >
              <FiGithub className="inline mb-1" size={13}/> Github
            </a>
          </li>
        </ul>
      </motion.div>
    </>
  );
};

export default Navbar;
