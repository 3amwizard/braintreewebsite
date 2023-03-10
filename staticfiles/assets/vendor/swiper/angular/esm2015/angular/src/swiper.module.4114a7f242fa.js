import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SwiperComponent } from './swiper.component';
import { SwiperSlideDirective } from './swiper-slide.directive';
import * as i0 from "@angular/core";
export class SwiperModule {
}
SwiperModule.ɵfac = i0.ɵɵngDeclareFactory({ minVersion: "12.0.0", version: "12.2.2", ngImport: i0, type: SwiperModule, deps: [], target: i0.ɵɵFactoryTarget.NgModule });
SwiperModule.ɵmod = i0.ɵɵngDeclareNgModule({ minVersion: "12.0.0", version: "12.2.2", ngImport: i0, type: SwiperModule, declarations: [SwiperComponent, SwiperSlideDirective], imports: [CommonModule], exports: [SwiperComponent, SwiperSlideDirective] });
SwiperModule.ɵinj = i0.ɵɵngDeclareInjector({ minVersion: "12.0.0", version: "12.2.2", ngImport: i0, type: SwiperModule, imports: [[CommonModule]] });
i0.ɵɵngDeclareClassMetadata({ minVersion: "12.0.0", version: "12.2.2", ngImport: i0, type: SwiperModule, decorators: [{
            type: NgModule,
            args: [{
                    declarations: [SwiperComponent, SwiperSlideDirective],
                    exports: [SwiperComponent, SwiperSlideDirective],
                    imports: [CommonModule],
                }]
        }] });
