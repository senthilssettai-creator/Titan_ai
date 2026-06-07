export default function Dashboard() {
  return (
    <aside className="space-y-6 rounded-3xl border border-slate-800 bg-slate-900/90 p-6 shadow-xl shadow-slate-950/20">
      <div>
        <h2 className="text-2xl font-semibold">Dashboard</h2>
        <p className="text-sm text-slate-500">Task overview and system status.</p>
      </div>
      <div className="grid gap-4">
        <div className="rounded-3xl bg-slate-950 p-5">
          <h3 className="text-base font-semibold text-slate-100">System status</h3>
          <p className="mt-2 text-sm text-slate-400">Backend API online, Gemini connectivity configured, memory enabled.</p>
        </div>
        <div className="rounded-3xl bg-slate-950 p-5">
          <h3 className="text-base font-semibold text-slate-100">Active agents</h3>
          <ul className="mt-3 space-y-2 text-sm text-slate-400">
            <li>Planner Agent</li>
            <li>Memory Agent</li>
            <li>Browser Agent</li>
            <li>Desktop Agent</li>
          </ul>
        </div>
      </div>
    </aside>
  );
}
