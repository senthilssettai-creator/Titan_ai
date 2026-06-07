import ChatPanel from "./components/ChatPanel";
import Dashboard from "./components/Dashboard";

export default function Home() {
  return (
    <main className="min-h-screen p-6">
      <div className="mx-auto max-w-7xl">
        <div className="mb-8 space-y-4">
          <h1 className="text-4xl font-semibold">TITAN AI</h1>
          <p className="text-slate-400">Your autonomous desktop AI agent.</p>
        </div>
        <div className="grid gap-6 xl:grid-cols-[1.5fr_1fr]">
          <ChatPanel />
          <Dashboard />
        </div>
      </div>
    </main>
  );
}
