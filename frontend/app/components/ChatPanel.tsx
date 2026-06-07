export default function ChatPanel() {
  return (
    <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-6 shadow-xl shadow-slate-950/20">
      <div className="flex items-center justify-between pb-4">
        <div>
          <h2 className="text-2xl font-semibold">Chat</h2>
          <p className="text-sm text-slate-500">Talk to Titan and start planning tasks.</p>
        </div>
      </div>
      <div className="space-y-4">
        <div className="rounded-2xl bg-slate-950 p-5 text-slate-300">
          <p className="text-slate-400">Type a goal such as “Create a YouTube video about Fortnite updates.”</p>
        </div>
        <textarea
          className="w-full rounded-2xl border border-slate-800 bg-slate-950 p-4 text-slate-100 outline-none focus:border-slate-500"
          rows={6}
          placeholder="Enter your goal..."
        />
        <button className="inline-flex rounded-2xl bg-indigo-500 px-5 py-3 text-sm font-semibold text-white transition hover:bg-indigo-400">
          Submit goal
        </button>
      </div>
    </section>
  );
}
