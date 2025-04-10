import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/posts/")({
  component: Posts,
});

function Posts() {
  return <div className="p-2">Hello from posts!</div>;
}
