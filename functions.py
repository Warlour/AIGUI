import torch
from diffusers import StableDiffusionPipeline
device = 'cuda'

def openjourney(prompt:str, negative_prompt:str = None, guidance_scale:float = 7.5, count:int = 1, seed:int = None, steps:int = 50, width:int = 512, height:int = 512) -> dict:
    files = {}

    try:
        model_id = r"C:/Users/mathi/Documents/python/AIBot/models/openjourney"
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to(device)
        generator = torch.Generator(device)

        generator = generator.manual_seed(seed) if seed else generator.manual_seed(generator.seed())
        
        outputtext = f"**Text prompt:** {prompt}\n"
        outputtext += f"**Negative text prompt:** {negative_prompt}\n"
        outputtext += f"**Count:** {count}\n"
        outputtext += f"**Seed:**  {generator.initial_seed()}\n"
        outputtext += f"**Guidance scale:** {guidance_scale}\n"
        outputtext += f"**Steps:** {steps}\n"
        outputtext += f"**Size:** {width}x{height}\n"

        filename = f"{generator.initial_seed()}_{guidance_scale}-{steps}.png"

        result = pipe(
            prompt=prompt, 
            negative_prompt=negative_prompt, 
            guidance_scale=guidance_scale,
            num_images_per_prompt=count, 
            num_inference_steps=steps,
            width=width,
            height=height,
            generator=generator
        )
        
        for i, image in enumerate(result.images):
            # If NSFW Detected
            if result.nsfw_content_detected[i] == True:
                outputtext += f"NSFW detected on image {i + 1} of {count}\n"

            name = f"{i+1}_{filename}"
            image.save(name, 'PNG')
            files[name] = f"Prompt: {prompt}\nNegative prompt: {negative_prompt}"
    except RuntimeError as e:
        if 'out of CUDA out of memory' in str(e):
            outputtext += f"Out of memory: try another prompt"
    
    return files