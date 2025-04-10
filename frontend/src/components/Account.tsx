import { useNavigate } from "@tanstack/react-router";
import { Button } from "./ui/button";

const Account = () => {
  const navigate = useNavigate();

  function handleRedirect(): void {
    navigate({ to: "/users/create" });
  }

  return (
    <section className="flex justify-items-center items-center z-10">
      <Button onClick={handleRedirect}>Account</Button>
    </section>
  );
};
export default Account;
