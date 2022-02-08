import { motion } from 'framer-motion';
import React, { useState } from 'react';
import {HiOutlineMenu} from "react-icons/hi"
const Navbar = () => {
    const [open,setOpen] = useState(false);
    const toggleMenu =  () => {
        setOpen(!open);
    }
    const barVariants = {
        open: { opacity: 1 },
        closed: { opacity: 0 },
    }
  return <nav className="bg-gradient-to-l from-gray-200 via-emerald-50 to-emerald-200 border-gray-200 px-2 sm:px-4 py-2.5 rounded">
      <div className="container flex flex-wrap justify-between items-center mx-auto">
            <a href="/" className="flex self-center text-lg font-semibold whitespace-nowrap">Algo Broker</a>
            <button onClick={toggleMenu} className="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-emerald-100 focus:outline-none focus:ring-2 focus:ring-emerald-200">
                <HiOutlineMenu size="20"/>
            </button>
            <div className="hidden w-full md:block md:w-auto">
                <ul className="flex flex-col mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium">
                    <li>
                        <a href="/" className="block transition py-2 pr-4 pl-3 text-black hover:bg-blue-100 rounded md:bg-transparent md:text-blue-900 md:px-2 ">
                            Home
                        </a>
                    </li>
                    <li>
                        <a href="/" className="block transition py-2 pr-4 pl-3 text-black hover:bg-blue-100 rounded md:bg-transparent md:text-blue-900 md:px-2 ">
                            Trade
                        </a>
                    </li>
                    <li>
                        <a href="/" className="block transition py-2 pr-4 pl-3 text-black hover:bg-blue-100 rounded md:bg-transparent md:text-blue-800 md:px-2 ">
                            Github
                        </a>
                    </li>
                    
                </ul>
            </div>
            <motion.div animate={open?"open":"closed"} variants={barVariants} className={`${open?'':'hidden'} w-full md:hidden`}>
                <ul className="flex flex-col mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium">
                    <li>
                        <a href="/" className="block transition py-2 pr-4 pl-3 text-black hover:bg-blue-100 rounded md:bg-transparent md:text-blue-900 md:px-2 ">
                            Home
                        </a>
                    </li>
                    <li>
                        <a href="/" className="block transition py-2 pr-4 pl-3 text-black hover:bg-blue-100 rounded md:bg-transparent md:text-blue-900 md:px-2 ">
                            Trade
                        </a>
                    </li>
                    <li>
                        <a href="/" className="block transition py-2 pr-4 pl-3 text-black hover:bg-blue-100 rounded md:bg-transparent md:text-blue-800 md:px-2 ">
                            Github
                        </a>
                    </li>
                    
                </ul>
            </motion.div>
      </div>
  </nav>;
};

export default Navbar;
