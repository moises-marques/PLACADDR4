import flet as ft 
import asyncio

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE
    
    async def animate(e = None):
        while True:
            img.offset.y = -0.3
            img.scale.scale = 2.9
            img.opacity = 1
            img.rotate.angle = 0.2
            img.update()
            await asyncio.sleep(6)
            
            img.offset.y = 1
            img.scale.scale = 0
            img.opacity = 0
            img.rotate.angle = 0
            img.update()
            await asyncio.sleep(4)
            
            
    
    img = ft.Image(
        src='Placa ddr4.png',
        offset=ft.Offset(x=0, y=0),
        scale=ft.Scale(scale=1),
        opacity = 0,
        rotate=ft.Rotate(angle=0),
        animate_offset=ft.Animation(duration=4000, curve=ft.AnimationCurve.EASE),
        animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.EASE),
        animate_opacity=ft.Animation(duration=3000, curve=ft.AnimationCurve.EASE),
        animate_rotation=ft.Animation(duration=4000, curve=ft.AnimationCurve.EASE),
        
    )
    
    page.add(img)
    
    asyncio.run(animate())
    
    # page.run_task(animate)
    
if __name__ == '__main__':
    ft.app(target = main)   