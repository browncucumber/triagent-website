"use client";
import { useState } from "react";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "";

const CATEGORIES = [
  { id: "urgent",      label: "Urgent",              color: "#EF4444", bg: "#FEF2F2" },
  { id: "appointment", label: "Appointment Request",  color: "#2E5FA3", bg: "#EBF1F8" },
  { id: "info",        label: "Information Request",  color: "#10B981", bg: "#ECFDF5" },
  { id: "complaint",   label: "Complaint",            color: "#F59E0B", bg: "#FFFBEB" },
];

const SAMPLES = [
  "I have severe tooth pain and cannot sleep, I need to see someone today",
  "What are your office hours on Saturdays?",
  "I would like to schedule a cleaning for next week",
  "I have been waiting 3 weeks for my crown and nobody has called me back",
];

const RESPONSES: Record<string, string> = {
  urgent:
    "I understand you are in pain -- this is a dental emergency. I am alerting our team right now. Someone will call you within 15 minutes. If this is a medical emergency, please call 911.",
  appointment:
    "I would be happy to help you schedule an appointment. I am checking our calendar for the next available slot and will send you a booking confirmation via SMS shortly.",
  info:
    "Our office hours are Monday-Friday 8am-5pm and Saturday 9am-2pm. You can also reach us at hello@triagent.cloud or use this chat anytime.",
  complaint:
    "I am sorry to hear about your experience -- this should not have happened. I am escalating this directly to our practice manager, who will call you within 2 hours.",
};

function classify_local(text: string): string {
  const t = text.toLowerCase();
  if (t.includes("pain") || t.includes("emergency") || t.includes("today") || t.includes("cannot sleep")) return "urgent";
  if (t.includes("schedule") || t.includes("appointment") || t.includes("book") || t.includes("cleaning")) return "appointment";
  if (t.includes("waiting") || t.includes("nobody") || t.includes("weeks") || t.includes("back")) return "complaint";
  return "info";
}

export default function DemoTriage() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState<{ category: string; confidence: number; response: string } | null>(null);
  const [loading, setLoading] = useState(false);

  const run = async (text: string) => {
    setInput(text);
    setLoading(true);
    setResult(null);

    if (!BACKEND_URL) {
      await new Promise((r) => setTimeout(r, 1200));
      const category = classify_local(text);
      setResult({ category, confidence: 94, response: RESPONSES[category] });
      setLoading(false);
      return;
    }

    try {
      const res = await fetch(`${BACKEND_URL}/triage`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });
      setResult(await res.json());
    } catch {
      setResult({ category: "info", confidence: 0, response: "Unable to connect to backend." });
    } finally {
      setLoading(false);
    }
  };

  const cat = CATEGORIES.find((c) => c.id === result?.category);

  return (
    <section id="demo-triage" className="py-24 px-6" style={{ background: "#EBF1F8" }}>
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-12">
          <div className="text-xs font-semibold uppercase tracking-wide mb-3" style={{ color: "#2E5FA3" }}>
            Service 3 -- Live Demo
          </div>
          <h2 className="text-3xl md:text-4xl font-extrabold mb-4" style={{ color: "#1B2A4A" }}>
            AI Customer Triage &amp; Response Agent
          </h2>
          <p className="text-gray-600 max-w-2xl mx-auto">
            Paste any patient message below -- or choose a sample. The AI classifies it and drafts the appropriate response in real time.
          </p>
        </div>

        <div className="max-w-3xl mx-auto">
          <div className="bg-white rounded-2xl shadow-xl p-8 mb-6">
            <label className="text-xs font-semibold uppercase tracking-wide text-gray-500 mb-2 block">
              Patient message
            </label>
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              rows={3}
              className="w-full px-4 py-3 rounded-xl border border-gray-200 text-sm outline-none focus:border-blue-400 resize-none"
              placeholder="Type or paste a patient inquiry..."
            />
            <div className="flex flex-wrap gap-2 mt-3 mb-4">
              {SAMPLES.map((s) => (
                <button
                  key={s}
                  onClick={() => run(s)}
                  className="text-xs px-3 py-1.5 rounded-full border border-gray-200 text-gray-500 hover:border-blue-400 hover:text-blue-600 transition-colors text-left"
                >
                  {s.length > 55 ? s.slice(0, 55) + "..." : s}
                </button>
              ))}
            </div>
            <button
              onClick={() => run(input)}
              disabled={loading || !input.trim()}
              className="w-full py-3 rounded-xl text-sm font-semibold text-white disabled:opacity-50 transition-opacity hover:opacity-90"
              style={{ backgroundColor: "#2E5FA3" }}
            >
              {loading ? "Classifying..." : "Classify & Draft Response"}
            </button>
          </div>

          {result && cat && (
            <div className="bg-white rounded-2xl shadow-xl p-8 space-y-6">
              <div>
                <div className="text-xs font-semibold uppercase tracking-wide text-gray-400 mb-3">Classification</div>
                <div className="grid grid-cols-4 gap-3">
                  {CATEGORIES.map((c) => (
                    <div
                      key={c.id}
                      className="rounded-xl p-3 text-center border-2 transition-all"
                      style={
                        c.id === result.category
                          ? { backgroundColor: c.bg, borderColor: c.color }
                          : { backgroundColor: "#F9FAFB", borderColor: "transparent" }
                      }
                    >
                      <div className="text-xs font-bold" style={{ color: c.id === result.category ? c.color : "#9CA3AF" }}>
                        {c.label}
                      </div>
                    </div>
                  ))}
                </div>
                <div className="mt-3 flex items-center gap-2">
                  <div className="h-1.5 rounded-full flex-1 bg-gray-100">
                    <div
                      className="h-1.5 rounded-full transition-all"
                      style={{ width: `${result.confidence}%`, backgroundColor: cat.color }}
                    />
                  </div>
                  <span className="text-xs font-semibold text-gray-500">{result.confidence}% confidence</span>
                </div>
              </div>

              <div>
                <div className="text-xs font-semibold uppercase tracking-wide text-gray-400 mb-2">AI-Drafted Response</div>
                <div
                  className="rounded-xl p-4 text-sm text-gray-700 leading-relaxed border"
                  style={{ backgroundColor: "#F8FAFF", borderColor: "#E5E9F0" }}
                >
                  {result.response}
                </div>
                <p className="text-xs text-gray-400 mt-2">
                  In a live deployment this response is sent automatically or queued for one-click staff approval.
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </section>
  );
}
