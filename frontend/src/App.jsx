import Navbar from "./components/navbar";
import {BrowserRouter,Routes,Route} from "react-router-dom";
import { AddLP, Home, Swap } from "./pages";

const App = () => {
  return (
    <BrowserRouter>
    <Navbar />
      <div className="bg-gray-50 min-h-screen">
      <Routes>
      <Route path="/" element={<Home/>} />
      <Route path="/addlp" element={<AddLP/>} />
      <Route path="/swap" element={<Swap/>} />
      </Routes>
      </div>
    </BrowserRouter>
  );
};

export default App;
