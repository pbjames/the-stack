import { NotepadText } from "lucide-react";
import Account from "./Account";
import { useNavigate } from "@tanstack/react-router";

const Header = () => {
  const navigate = useNavigate();
  function handleNavigate(): void {
    navigate({ to: "/" });
  }
  return (
    <header className="z-0 w-full top-0 bg-gray-300 h-16">
      <img
        src="https://www.pixelstalk.net/wp-content/uploads/2016/06/Lightning-Wallpapers-HD.jpg"
        className="object-cover w-full h-16 opacity-30 absolute grayscale z-0"
      />
      <nav className="flex flex-row justify-items-start items-center space-x-2 overflow-hidden h-16 p-4">
        <NotepadText className="h-7 w-7 z-10" onClick={handleNavigate} />
        <text
          className="text-2xl font-black text-nowrap z-10"
          onClick={handleNavigate}
        >
          Todo Pro
        </text>
        <div className="w-full" />
        <Account />
      </nav>
    </header>
  );
};

//
//<div className="p-2 flex gap-2">
//  <Link to="/" className="[&.active]:font-bold">
//    Home
//  </Link>{" "}
//  <Link to="/about" className="[&.active]:font-bold">
//    About
//  </Link>
//</div>
export default Header;
