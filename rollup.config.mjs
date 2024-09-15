import { nodeResolve } from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import { terser } from 'rollup-plugin-terser';
import scss from 'rollup-plugin-scss'


export default {
    input: {
        main: './core/static/scripts/app.js',
    },
    output: {
        dir: './core/static/scripts/compiled/',
        format: 'esm',
        sourcemap: true,
        entryFileNames: '[name].min.js',
        chunkFileNames: '[name]-[hash].min.js',
    },
    plugins: [
        nodeResolve(),
        commonjs(),
        terser({
            ecma: 8,
            safari10: true,
            compress: {
                keep_fnames: true,
                defaults: true,
                arguments: true,
                booleans: true,
                collapse_vars: true,
                conditionals: true,
                dead_code: true,
                drop_console: false,
                drop_debugger: true,
                evaluate: true,
                expression: false,
                hoist_funs: false,
                hoist_props: true,
                hoist_vars: false,
                if_return: true,
                inline: true,
                join_vars: true,
                keep_infinity: true,
                loops: true,
                negate_iife: true,
                passes: 5,
                properties: true,
                reduce_funcs: true,
                reduce_vars: true,
                sequences: true,
                side_effects: true,
                switches: true,
                toplevel: false,
                typeofs: true,
                unsafe: false,
                unsafe_comps: false,
                unsafe_math: false,
                unsafe_proto: false,
                unused: true,
                warnings: true
            },
            format: {
            comments: false,
            },
            mangle: {
            keep_fnames: true,
            },
        }),
        scss({
            output: './core/static/styles/main.min.css',
            outputStyle: "compressed",
        })
    ],
    watch: {
        clearScreen: false,
    },
    cache: true, // Включаем кэширование
    treeshake: true, // Включаем уборку лишних функций
};