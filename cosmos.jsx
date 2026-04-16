import { useMemo, useState } from 'react';
import { motion } from 'framer-motion';
import { ArrowUpRight, Globe, Orbit, Rocket, Sparkles, Stars } from 'lucide-react';

export default function CosmosProject() {
  const [activePlanet, setActivePlanet] = useState('NOVA');

  const planets = [
    {
      id: 'NOVA',
      name: 'NOVA',
      subtitle: 'Launch portal',
      description:
        'A cinematic entry point with a glowing planet, deep-space gradients, and a founder-style presentation layer built to feel unforgettable.',
      position: 'left-[12%] top-[24%]',
      size: 'h-28 w-28 md:h-36 md:w-36',
      glow: 'from-fuchsia-500 via-violet-500 to-cyan-400',
    },
    {
      id: 'AETHER',
      name: 'AETHER',
      subtitle: 'Future systems',
      description:
        'An abstract world for futuristic interfaces, immersive motion, and product concepts that feel larger than standard portfolio cards.',
      position: 'right-[18%] top-[18%]',
      size: 'h-24 w-24 md:h-32 md:w-32',
      glow: 'from-cyan-400 via-sky-500 to-blue-600',
    },
    {
      id: 'SOLARA',
      name: 'SOLARA',
      subtitle: 'Luxury experience',
      description:
        'A rich visual zone for dark premium branding, elegant storytelling, and pages that feel more like launch campaigns than student work.',
      position: 'left-[22%] bottom-[16%]',
      size: 'h-20 w-20 md:h-28 md:w-28',
      glow: 'from-amber-300 via-orange-500 to-rose-500',
    },
    {
      id: 'VOID-X',
      name: 'VOID-X',
      subtitle: 'Experimental lab',
      description:
        'A high-contrast visual playground for bold experiments, intense color bursts, and creative coding concepts with strong identity.',
      position: 'right-[14%] bottom-[20%]',
      size: 'h-24 w-24 md:h-32 md:w-32',
      glow: 'from-emerald-400 via-teal-400 to-cyan-400',
    },
  ];

  const stars = useMemo(
    () =>
      Array.from({ length: 65 }, (_, i) => ({
        id: i,
        left: `${Math.random() * 100}%`,
        top: `${Math.random() * 100}%`,
        size: `${Math.random() * 3 + 1}px`,
        delay: `${Math.random() * 3}s`,
        duration: `${Math.random() * 4 + 2}s`,
      })),
    []
  );

  const current = planets.find((planet) => planet.id === activePlanet) ?? planets[0];

  return (
    <div className="relative min-h-screen overflow-hidden bg-[#030712] text-white">
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_left,_rgba(168,85,247,0.22),_transparent_24%),radial-gradient(circle_at_top_right,_rgba(34,211,238,0.16),_transparent_22%),radial-gradient(circle_at_bottom,_rgba(251,146,60,0.14),_transparent_20%)]" />
      <div className="absolute left-[-8rem] top-24 h-72 w-72 rounded-full bg-fuchsia-500/20 blur-3xl" />
      <div className="absolute right-[-10rem] top-32 h-96 w-96 rounded-full bg-cyan-400/10 blur-3xl" />
      <div className="absolute bottom-[-8rem] left-1/3 h-80 w-80 rounded-full bg-orange-400/10 blur-3xl" />

      {stars.map((star) => (
        <motion.span
          key={star.id}
          className="absolute rounded-full bg-white/80"
          style={{ left: star.left, top: star.top, width: star.size, height: star.size }}
          animate={{ opacity: [0.25, 1, 0.25], scale: [1, 1.4, 1] }}
          transition={{ repeat: Infinity, duration: Number.parseFloat(star.duration), delay: Number.parseFloat(star.delay) }}
        />
      ))}

      <main className="relative z-10 mx-auto max-w-7xl px-6 py-8 md:px-10 lg:px-12">
        <motion.section
          initial={{ opacity: 0, y: 18 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
          className="relative overflow-hidden rounded-[36px] border border-white/10 bg-white/[0.04] p-6 shadow-[0_30px_120px_rgba(0,0,0,0.45)] backdrop-blur-2xl md:p-10"
        >
          <div className="absolute inset-0 bg-[linear-gradient(135deg,rgba(255,255,255,0.05),transparent_30%,transparent_70%,rgba(255,255,255,0.03))]" />

          <div className="relative z-10 flex flex-wrap items-center justify-between gap-4">
            <div className="inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/5 px-4 py-2 text-xs uppercase tracking-[0.28em] text-white/70">
              <Sparkles className="h-4 w-4 text-cyan-300" />
              COSMOS / Interactive Universe
            </div>
            <div className="rounded-full border border-white/10 bg-black/20 px-4 py-2 text-sm text-white/60">
              Visual Experience Project
            </div>
          </div>

          <div className="relative z-10 mt-10 grid gap-10 lg:grid-cols-[1.1fr_0.9fr] lg:items-end">
            <div>
              <div className="text-sm uppercase tracking-[0.32em] text-fuchsia-300/75">Independent concept / Not related to StudyAI</div>
              <h1 className="mt-4 max-w-5xl text-5xl font-black leading-[0.9] tracking-[-0.05em] md:text-7xl">
                COSMOS — a
                <span className="bg-gradient-to-r from-fuchsia-400 via-violet-300 to-cyan-300 bg-clip-text text-transparent"> visual feast </span>
                built like a digital universe.
              </h1>
              <p className="mt-6 max-w-2xl text-base leading-8 text-white/68 md:text-lg">
                This is a fully separate concept project: immersive space atmosphere, floating planets, cinematic glow, and a premium landing experience designed to make your portfolio unforgettable.
              </p>

              <div className="mt-8 flex flex-wrap gap-3">
                <a
                  href="https://studyai-x.streamlit.app/"
                  target="_blank"
                  className="inline-flex items-center gap-2 rounded-full bg-white px-6 py-3 text-sm font-semibold text-black transition hover:scale-[1.02]"
                >
                  Visit Website
                  <ArrowUpRight className="h-4 w-4" />
                </a>
                <button className="rounded-full border border-white/15 bg-white/5 px-6 py-3 text-sm font-semibold text-white transition hover:bg-white/10">
                  Explore Universe
                </button>
              </div>

              <div className="mt-6 flex items-center gap-2 text-sm text-cyan-300">
                <Globe className="h-4 w-4" />
                Website linked inside the project
              </div>
              <div className="mt-2 break-all text-xs text-white/45">https://studyai-x.streamlit.app/</div>
            </div>

            <div className="grid gap-4 sm:grid-cols-3 lg:grid-cols-1 xl:grid-cols-3">
              {[
                { icon: Orbit, value: '04', label: 'Interactive planets' },
                { icon: Stars, value: '65+', label: 'Animated stars' },
                { icon: Rocket, value: 'Ultra', label: 'Visual impact' },
              ].map((item, idx) => {
                const Icon = item.icon;
                return (
                  <motion.div
                    key={item.label}
                    initial={{ opacity: 0, y: 16 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.15 * idx, duration: 0.5 }}
                    className="rounded-[24px] border border-white/10 bg-black/20 p-5 backdrop-blur-md"
                  >
                    <Icon className="h-5 w-5 text-cyan-300" />
                    <div className="mt-4 text-3xl font-black tracking-tight">{item.value}</div>
                    <div className="mt-2 text-sm text-white/60">{item.label}</div>
                  </motion.div>
                );
              })}
            </div>
          </div>
        </motion.section>

        <section className="relative mt-10 min-h-[620px] overflow-hidden rounded-[36px] border border-white/10 bg-white/[0.03] backdrop-blur-2xl">
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_rgba(255,255,255,0.05),_transparent_42%)]" />
          <div className="absolute left-1/2 top-1/2 h-[340px] w-[340px] -translate-x-1/2 -translate-y-1/2 rounded-full border border-white/10 bg-[radial-gradient(circle_at_30%_30%,rgba(255,255,255,0.18),rgba(255,255,255,0.03)_35%,transparent_65%)] shadow-[0_0_120px_rgba(168,85,247,0.15)]" />
          <div className="absolute left-1/2 top-1/2 h-[520px] w-[520px] -translate-x-1/2 -translate-y-1/2 rounded-full border border-white/5" />
          <div className="absolute left-1/2 top-1/2 h-[700px] w-[700px] -translate-x-1/2 -translate-y-1/2 rounded-full border border-white/[0.03]" />

          {planets.map((planet, idx) => (
            <motion.button
              key={planet.id}
              onClick={() => setActivePlanet(planet.id)}
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: activePlanet === planet.id ? 1.08 : 1 }}
              transition={{ delay: 0.12 * idx, duration: 0.45 }}
              className={`absolute ${planet.position} ${planet.size} group rounded-full border border-white/20 shadow-[0_0_60px_rgba(255,255,255,0.06)]`}
            >
              <div className={`absolute inset-0 rounded-full bg-gradient-to-br ${planet.glow} opacity-85 blur-[2px] transition duration-300 group-hover:scale-105`} />
              <div className="absolute inset-[2px] rounded-full bg-[#0a1020]/40 backdrop-blur-md" />
              <div className="relative z-10 flex h-full w-full items-center justify-center text-center">
                <div>
                  <div className="text-sm font-black tracking-[0.22em] text-white">{planet.name}</div>
                  <div className="mt-1 text-[10px] uppercase tracking-[0.2em] text-white/60">{planet.subtitle}</div>
                </div>
              </div>
            </motion.button>
          ))}

          <motion.div
            key={current.id}
            initial={{ opacity: 0, y: 18 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.45 }}
            className="absolute bottom-6 left-6 right-6 rounded-[28px] border border-white/10 bg-[#060b18]/80 p-6 shadow-[0_20px_80px_rgba(0,0,0,0.35)] backdrop-blur-2xl md:left-10 md:right-10 md:p-8"
          >
            <div className="grid gap-8 lg:grid-cols-[1fr_0.8fr] lg:items-end">
              <div>
                <div className="text-xs uppercase tracking-[0.28em] text-cyan-300/80">Selected planet</div>
                <h2 className="mt-4 text-3xl font-black tracking-[-0.03em] md:text-4xl">{current.name}</h2>
                <div className="mt-2 text-sm uppercase tracking-[0.22em] text-white/45">{current.subtitle}</div>
                <p className="mt-5 max-w-2xl text-sm leading-8 text-white/68 md:text-base">{current.description}</p>
              </div>

              <div className="rounded-[24px] border border-white/10 bg-white/[0.04] p-5">
                <div className="text-xs uppercase tracking-[0.24em] text-fuchsia-300/75">Project website</div>
                <div className="mt-4 flex items-center gap-2 text-cyan-300">
                  <Globe className="h-4 w-4" />
                  <span className="text-sm font-medium">Linked inside this independent project</span>
                </div>
                <div className="mt-3 break-all text-xs text-white/50">https://studyai-x.streamlit.app/</div>
                <a
                  href="https://studyai-x.streamlit.app/"
                  target="_blank"
                  className="mt-5 inline-flex items-center gap-2 rounded-full bg-white px-5 py-3 text-sm font-semibold text-black transition hover:scale-[1.02]"
                >
                  Open Website
                  <ArrowUpRight className="h-4 w-4" />
                </a>
              </div>
            </div>
          </motion.div>
        </section>
      </main>
    </div>
  );
}
