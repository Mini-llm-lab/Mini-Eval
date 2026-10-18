# Results: small_lm

Zero-shot suite chosen to give signal on models under 1B parameters.

Protocol v1, lm-eval 0.4.13, 0-shot. Values are the primary metric of each task with their standard error.

| Model | Non-embedding params | Tokens seen | hellaswag (acc_norm) | arc_easy (acc_norm) | arc_challenge (acc_norm) | piqa (acc_norm) | winogrande (acc) | openbookqa (acc_norm) | sciq (acc_norm) | lambada_openai (acc) | wikitext (bits_per_byte) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| pythia-70m-step143000 | 18.9M | 299.89B | 0.274 ± 0.004 | 0.353 ± 0.010 | 0.218 ± 0.012 | 0.592 ± 0.011 | 0.529 ± 0.014 | 0.254 ± 0.019 | 0.564 ± 0.016 | 0.227 ± 0.006 | 1.080 |
| SmolLM2-135M | 106.2M | 2000.00B | 0.431 ± 0.005 | 0.586 ± 0.010 | 0.296 ± 0.013 | 0.685 ± 0.011 | 0.530 ± 0.014 | 0.334 ± 0.021 | 0.782 ± 0.013 | 0.429 ± 0.007 | 0.847 |
| mini-llm-34M-12000steps | 25.7M | 0.20B | 0.270 ± 0.004 | 0.333 ± 0.010 | 0.222 ± 0.012 | 0.548 ± 0.012 | 0.515 ± 0.014 | 0.250 ± 0.019 | 0.486 ± 0.016 | 0.137 ± 0.005 | 1.289 |
| mini-llm-70M-22000steps | 59.5M | 1.44B | 0.285 ± 0.005 | 0.405 ± 0.010 | 0.232 ± 0.012 | 0.586 ± 0.011 | 0.515 ± 0.014 | 0.278 ± 0.020 | 0.579 ± 0.016 | 0.197 ± 0.006 | 1.067 |
| mini-llm-150M-34332steps | 127.4M | 4.50B | 0.331 ± 0.005 | 0.472 ± 0.010 | 0.255 ± 0.013 | 0.628 ± 0.011 | 0.517 ± 0.014 | 0.304 ± 0.021 | 0.689 ± 0.015 | 0.280 ± 0.006 | 0.941 |
| Random guessing |  |  | 0.250 | 0.250 | 0.250 | 0.500 | 0.500 | 0.250 | 0.250 | 0.000 |  |

## Score against tokens seen

![](small_lm_vs_tokens.png)

## Score against non-embedding parameters

![](small_lm_vs_params.png)
